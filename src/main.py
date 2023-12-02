import asyncio, os
from aiogram import Bot, Dispatcher
from handlers import start
from dotenv import load_dotenv


# Запуск бота
async def main():
    load_dotenv(dotenv_path="./.env")
    print(os.getenv("BOT_TOKEN"))
    bot = Bot(token=str(os.environ.get("BOT_TOKEN")))
    dp = Dispatcher()

    dp.include_routers(start.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
