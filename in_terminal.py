from bot.parser import build_weather_report


def print_help() -> None:
    print("-" * 32)
    print("This is console weather app")
    print("0, q, exit - exit")
    print("1 - see weather")
    print("help - show this msg")
    print("-" * 32)


async def print_weather_report(address: str) -> None:
    print(await build_weather_report(address))


async def start_in_terminal() -> None:
    print_help()
    while True:
        ch: str = input("\n>> ")
        print()

        if ch in ["0", "q", "exit"]:
            break
        if ch == "help":
            print_help()
            continue

        if ch == "1":
            address: str = input("Enter location\n>> ")
            print("Waiting for answer...")
            print()
            await print_weather_report(address)
