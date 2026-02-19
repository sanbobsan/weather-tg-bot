import aiohttp
from datetime import datetime


async def geocode_with_nominatim(address):
    """
    Асинхронно преобразует адрес в координаты с помощью OpenStreetMap
    - "latitude": широта,
    - "longitude": долгота,
    - "address": место
    """

    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": address, "format": "json", "limit": 1}
    headers = {"User-Agent": "WeatherBot/1.0"}

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, headers=headers) as response:
                response.raise_for_status()
                data = await response.json()

        if not data:
            return None

        return {
            "latitude": float(data[0]["lat"]),
            "longitude": float(data[0]["lon"]),
            "address": data[0]["display_name"],
        }
    except Exception as e:
        print(f"Ошибка геокодирования: {e}")
        return None


async def get_weather(latitude, longitude):
    """
    Асинхронно получает прогноз погоды по координатам через Open-Meteo API
    """

    if not latitude or not longitude:
        return None

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,weather_code",
        "hourly": "temperature_2m,weather_code",
        "daily": "weather_code,temperature_2m_max,temperature_2m_min",
        "timezone": "auto",
        "forecast_days": 3,
    }

    try:
        async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=4)
        ) as session:
            async with session.get(url, params=params) as response:
                response.raise_for_status()
                return await response.json()

    except aiohttp.ClientError as e:
        print(f"!!! Ошибка !!! Не получилось получить погоду \n{e}")
        return None


def decode_weathercode(code):
    """
    Расшифровывает коды погоды WMO
    """

    weather_codes = {
        0: "Ясно ☀️",
        1: "Преимущественно ясно 🌤",
        2: "Переменная облачность ⛅",
        3: "Пасмурно ☁️",
        45: "Туман 🌫",
        48: "Инейный туман",
        51: "Легкая морось 🌧",
        53: "Умеренная морось",
        55: "Сильная морось",
        56: "Ледяная морось",
        57: "Сильная ледяная морось",
        61: "Слабый дождь 🌧",
        63: "Умеренный дождь",
        65: "Сильный дождь 💧",
        66: "Ледяной дождь",
        67: "Сильный ледяной дождь",
        71: "Слабый снег ❄️",
        73: "Умеренный снег",
        75: "Сильный снег",
        77: "Снежные зерна",
        80: "Слабый ливень 🌦",
        81: "Умеренный ливень",
        82: "Сильный ливень 💦",
        85: "Снегопад",
        86: "Сильный снегопад",
        95: "Гроза ⚡",
        96: "Гроза с градом 🌩",
        99: "Сильная гроза с градом",
    }

    return weather_codes.get(code, f"Неизвестный код погоды ({code})")


def compile_weather_data(weather_data, location_info):
    """
    Форматирует сырые данные о погоде в читаемый текст
    Возвращает многострочную строку с отчетом
    """

    if not weather_data:
        return None

    current = weather_data["current"]
    daily = weather_data["daily"]

    # Проверка наличия данных на сегодня
    if len(daily["time"]) == 0:
        return "Прогноз на сегодня недоступен"

    # Получаем данные на сегодня (индекс 0)
    date = datetime.strptime(daily["time"][0], "%Y-%m-%d").strftime("%d.%m.%Y")
    weather_code = daily["weather_code"][0]
    temp_max = daily["temperature_2m_max"][0]
    temp_min = daily["temperature_2m_min"][0]

    # Формируем результат
    result = [
        f"📍 Погода для: {location_info['address']}",
        f"📅 Дата: {date} (сегодня)",
        f"🌡️ Сейчас: {current['temperature_2m']}°C, {decode_weathercode(current['weather_code'])}",
        f"☀️ Днем: {decode_weathercode(weather_code)}",
        f"📈 Макс: {temp_max}°C",
        f"📉 Мин: {temp_min}°C",
        "\nПочасовой прогноз на сегодня:",
    ]

    # Добавляем почасовой прогноз на сегодня
    today_date = datetime.strptime(daily["time"][0], "%Y-%m-%d").date()

    for i, hour_time in enumerate(weather_data["hourly"]["time"]):
        hour_dt = datetime.strptime(hour_time, "%Y-%m-%dT%H:%M")

        # Пропускаем часы, не относящиеся к сегодняшнему дню
        if hour_dt.date() != today_date:
            continue

        hour = hour_dt.strftime("%H:%M")
        temp = weather_data["hourly"]["temperature_2m"][i]
        code = weather_data["hourly"]["weather_code"][i]
        result.append(f"- {hour}: {temp}°C, {decode_weathercode(code)}")

    return "\n".join(result)


async def build_weather_report(address: str):
    """
    Асинхронно возвращает готовый текст для сообщения
    """

    location = await geocode_with_nominatim(address)
    if not location or not location["latitude"]:
        print("!!! Ошибка !!! Не получилось получить координаты")
        return "❌ Ошибка геокодирования, укажите существующий адрес"

    weather = await get_weather(location["latitude"], location["longitude"])
    if not weather:
        return "❌ Ошибка. Погода на этот адрес не найдена"

    weather_data = compile_weather_data(weather, location)
    if not weather_data:
        return None

    return weather_data
