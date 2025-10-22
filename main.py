import asyncio
from aiogram import Bot, Dispatcher
from aiohttp import ServerDisconnectedError
from config import Config
from router import router

def check_token(func):
    def wrapper(*args, **kwargs):
        try:
            with open(".env", "r", encoding="utf-8") as file:
                for line in file:
                    if line.startswith("TG_TOKEN=") and line.strip().split("=", 1)[-1]:
                        # Токен найден, продолжаем выполнение функции
                        return func(*args, **kwargs)
        except FileNotFoundError:
            # Файла .env ещё нет
            pass

        # Если токена нет — предлагаем ввести и записать его
        token = input("Введите токен телеграмм бота: ")
        with open(".env", "w", encoding="utf-8") as file:
            file.write("TG_TOKEN=" + token)
        print("Токен сохранён в .env")
        return None  # Не выполняем функцию дальше после записи токена

    return wrapper

@check_token
async def start():
    config = Config()

    bot = Bot(config.tg_token)
    dp = Dispatcher()

    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        print("bot started")
        asyncio.run(start())
    except (KeyboardInterrupt):
        pass
    finally:
        print("bot closed")

