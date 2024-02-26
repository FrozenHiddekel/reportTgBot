from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession

from src.chat_support.models import ChatSupport


async def orm_add_chat_message(session: AsyncSession, data: dict):
    time = datetime.utcnow()
    obj = ChatSupport(
        body=data["body"],
        username=data["username"],
        tg_user_id=data["tg_user_id"],
        posted_at=time,
    )
    session.add(obj)
    await session.commit()
