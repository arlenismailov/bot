import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os
from app.handlers import router

# Загрузка токена из .env файла
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Проверка наличия токена
if not BOT_TOKEN:
    raise ValueError("Токен бота не найден! Проверьте файл .env.")

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def main():
    # Подключаем маршруты
    dp.include_router(router)
    try:
        print("Бот запущен!")
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен.")
