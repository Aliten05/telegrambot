import asyncio
import random
import pip
pip.main(['install', 'aiogram'])
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

TOKEN_API = "7055348284:AAGAFOeTUDj3-ri7UGgGjoyLNMU1Z3l7sjU"

bot = Bot(TOKEN_API, parse_mode='MarkdownV2')
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(f"иди нахуй *{message.from_user.first_name}*")


@dp.message(Command(commands=['rng', 'random', 'roll']))
async def rand(message: Message, command: CommandObject):
    print(command.args)
    if command.args is None:
        await message.answer(f'я твою мать ебал кстати, {random.randint(1, 100)}')
    else:
        L = command.args.split()
        if len(L) != 2:
            await message.answer(f'ты долбаеб, формат /roll число число, либо вместо ролла rng, random')
        else:
            a = L[0]
            b = L[1]
            if not a.isdigit() or not b.isdigit():
                await message.answer(f'ты долбаеб, формат /roll число число, либо вместо ролла rng, random')
            else:
                await message.answer(f'я твою мать ебал кстати, {random.randint(int(a), int(b))}')


@dp.message(Command('coach'))
async def dota(message: Message, command: CommandObject):
    l = [el for el in command.args.split()]
    await message.answer(f'ахахахахха ебать ||{l[random.randint(0, len(l) - 1)]}|| лох, тренером идет')


@dp.message(Command('DOXXSWATTXXX'))
async def DOXX(message: Message):
    for i in range(20):
        await message.reply('DOXXSWATT')


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
