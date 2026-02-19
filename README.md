# 🌤 Telegram Weather Bot

Простой Telegram бот для получения актуальной погоды на планете Земля

## 🚀 Возможности

- Почасовая температура и описание погоды на сегодня
- Поддержка любого адреса/места (геокодирование)

## 🛠 Использование

1. **Зависимости:**

   ```bash
   pip install -r requirements.txt
   ```

   - aiohttp
   - aiogram
   - python-decouple

2. **Переменные окружения (`.env`):**

   ```env
   TOKEN=your_telegram_bot_token
   ```

   так же, есть режим работы в терминале (без бота и токена):

   ```env
   TERMINAL=true
   ```

3. **Запуcк бота:**

   ```bash
   python main.py
   ```

## 🐳 Развёртывание в Docker

| Действие          | Режим        | Команда                                                              |
| ----------------- | ------------ | -------------------------------------------------------------------- |
| **Сборка образа** | —            | `docker build -t weather-tg-bot .`                                   |
| **Запуск бота**   | В терминале  | `docker run -e TERMINAL=1 -i --name weather-tg-bot weather-tg-bot`   |
| **Запуск бота**   | Телеграм бот | `docker run -d --env-file .env --name weather-tg-bot weather-tg-bot` |
| **Остановка**     | —            | `docker stop weather-tg-bot`                                         |
| **Удаление**      | —            | `docker rm weather-tg-bot`                                           |

## 🌐 Используемые API

| API                                                    | Назначение                            | Документация                                                     | API Key              |
| ------------------------------------------------------ | ------------------------------------- | ---------------------------------------------------------------- | -------------------- |
| [Telegram Bot API](https://core.telegram.org/bots/api) | Приём и отправка сообщений в Telegram | [Docs](https://core.telegram.org/bots/api)                       | ✅ Требуется `TOKEN` |
| [Nominatim (OpenStreetMap)](https://nominatim.org/)    | Геокодирование адресов в координаты   | [Docs](https://nominatim.org/release-docs/develop/api/Overview/) | ❌ Не требуется      |
| [Open-Meteo](https://open-meteo.com/)                  | Прогноз погоды по координатам         | [Docs](https://open-meteo.com/en/docs)                           | ❌ Не требуется      |

### ⚠️ Ограничения API

- **Telegram Bot API**: Получите токен у [@BotFather](https://t.me/BotFather), лимиты: ~30 сообщений/сек
- **Nominatim**: Максимум 1 запрос в секунду
- **Open-Meteo**: До 10 000 запросов в день (бесплатно)
