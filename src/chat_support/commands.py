from aiogram import types, Router
from aiogram.filters import CommandStart, Command
from sqlalchemy.ext.asyncio import AsyncSession
from src.openAI.chatGPT import chatGPT_help, chatGPT_glados
from src.orm.orm_chat_support import orm_add_chat_message

chat_support_router = Router()


@chat_support_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Данный бот создан для сохраненния жалоб через команду \"/report\", "
                         "а также для консультации с ИИ на базе gpt-3.5-turbo."
                         "Чтобы узнать особенности работы бота просто напишите свой вопрос в чат")


@chat_support_router.message(Command("гладос", "Гладос", "Glados", "GLaDOS", "glados"))
async def glados_cmd(message: types.Message):
    result = await chatGPT_glados(message.text)
    await message.answer(result)


@chat_support_router.message(Command("report"))
async def main_cmd(message: types.Message, session: AsyncSession):
    print(message.text)
    if message.text == "/report":
        print("asdas")
        await message.answer("После команды нужно написать непосредственно репорт. "
                             "И не кликай просто так на цветной текст, ты же не сорока")
    else:
        data = {'body': message.text, 'username': message.from_user.username, 'tg_user_id': message.from_user.id}
        await orm_add_chat_message(session, data)
        react = types.ReactionTypeEmoji(emoji="✍")
        await message.react([react])


@chat_support_router.message()
async def main_cmd(message: types.Message):
    result = await chatGPT_help(message.text)
    await message.answer(result)




