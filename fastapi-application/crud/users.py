from sqlalchemy.ext.asyncio import AsyncSession
from typing import Sequence
from core.models import User
from sqlalchemy import select
from core.schemas.user import UserCreate


async def get_all_users(session: AsyncSession) -> Sequence[User]:
    stmt = select(User).order_by(User.id)
    result = await session.scalars(stmt)
    return result.all()


async def create_user(
        session: AsyncSession,
        user_create: UserCreate,
) -> User:
    user = User(**user_create.model_dump())
    session.add(user)
    await session.commit()
    # await session.refresh()
    return user 