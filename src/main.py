print("[INFO]: Importing modules...")

import asyncio, time
from aiogram import Bot, Dispatcher
from handlers import basic

print("[INFO]: Modules imported successfuly!")


def xor(plain_text: bytes, key: bytes):
    pt = plain_text
    len_key = len(key)
    encoded = []
    for i in range(0, len(pt)):
        encoded.append(pt[i] ^ key[i % len_key])
    return bytes(encoded)


key = bytes(input("[REQUEST]: Enter key to decrypt token: "), 'utf-8') # getting key to encrypt token

BOT_TOKEN = ""

try:
    BOT_TOKEN = xor(open("src/config.dat", "rb").read(), key).decode('utf-8') # getting bot token
except Exception:
    print("[ERROR]: Key is incorrect!")




# Запуск бота
async def main():
    print("[INFO]: Bot init...")
    try:
        bot = Bot(token=BOT_TOKEN, parse_mode='HTML')

        print("[INFO]: Key is correct!")

        time.sleep(0.1)

        print("[INFO]: Setting dispatcher...")
        dp = Dispatcher() # setting dispatcher
        print("[INFO]: Dispatcher set successfuly!")

        time.sleep(0.1)

        print("[INFO]: Including routers...")
        dp.include_routers(basic.router) # including routers
        print("[INFO]: Routers included succesfuly!")

        time.sleep(0.1)

        print("[INFO]: Deleting webhooks...")
        await bot.delete_webhook(drop_pending_updates=True) # deleting webhooks
        print("[INFO]: Webhooks deleted successfuly!")

        time.sleep(0.1)

        print("[INFO]: Starting bot...") # strating bot
        await dp.start_polling(bot)

        print("[INFO]: Deactivation bot...")
        print("[INFO]: Bot deactivated successfuly!") 
    except Exception as e:
        print("[ERROR]: " + str(e))

if __name__ == "__main__":
    asyncio.run(main())

print("[INFO]: Exit out of program.")
