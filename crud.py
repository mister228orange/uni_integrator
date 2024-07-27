from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import PreanalyticsInvitro as Order


async def create_order(session: AsyncSession, order: Order):
    session.add(order)
    await session.commit()
    await session.refresh(order)
    return order


async def get_order(session: AsyncSession, order_id: int):
    result = await session.execute(select(Order).where(Order.order_id == order_id))
    return result.scalars().first()


async def get_incomplete_orders_ids(session: AsyncSession):
    result = await session.execute(select(Order.order_id).where(Order.status != Order.StatusEnum.COMPLETE))
    return result.scalars().all()


async def update_order(session: AsyncSession, order_id: int, **kwargs):
    result = await session.execute(select(Order).where(Order.order_id == order_id))
    order = result.scalars().first()
    for key, value in kwargs.items():
        setattr(order, key, value)
    await session.commit()
    return order
