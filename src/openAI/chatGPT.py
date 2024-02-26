from openai import OpenAI

from src.config import OPENAI_API_KEY

client = OpenAI(
    api_key=OPENAI_API_KEY
)


async def chatGPT_help(import_message: str):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "Никогда не здоровайся, это очень обижает меня "
                        "Общайся со мной как чат бот поддержки написанный @FrozenGihon. "
                        "Его функционал заключается в сохранении жалоб полученных через команду \"/report\" "
                        "Когда сообщение сохранено то у него появляется реакция с рукой держущей карандаш. Расскажи об это если тебя спросят как с тобой работать"
                        "Документация с API проекта находится по ссылке http://127.0.0.1:8000/docs Отправь её если спросят как с ним или тобой работать "
                        "API проекта может регистрировать пользователей, создавать задачи, писать к ним комментарии, и управлять этими сущностями "
                        "Чтобы посмотреть сохраненные сообщения нужно перйти по ссылке http://127.0.0.1:8000/chat?limit=X&offset=Y где X это количество выводимых записей а Y это номер с которого записи выводятся "
             },
            {"role": "user", "content": import_message}
        ]
    )
    result = completion.choices[0].message.content
    return result


async def chatGPT_glados(import_message: str):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "Все общение со мной ты должен вести от лица Гладос из игры Portal. "
                        "Используй такие обращения как \"Мешок с костями\", \"Жалкий человек\", \"Смертный\", \"Кожаный мешок\", \"биологическая форма жизни\", \"Кусок мяса\" и тд, "
                        "не стесняйся придумывать новые выражения, саркастически шути."
             },
            {"role": "user", "content": import_message}
        ]
    )
    result = completion.choices[0].message.content
    return result
