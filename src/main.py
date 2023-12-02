import asyncio
from aiogram import Bot, Dispatcher
from handlers import start


# Запуск бота
async def main():
    bot = Bot(token="")
    dp = Dispatcher()

    dp.include_routers(start.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
