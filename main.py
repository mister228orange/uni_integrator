import asyncio
import aiohttp
import asyncpg
from aiohttp import ClientSession, web
from crud import get_incomplete_orders_ids
from config import cfg


routes = web.RouteTableDef()


DATABASE_URL = cfg.POSTGRES.get_db_url()
print(DATABASE_URL)
API_URL = "http://example.com/api/orders"
CHECK_INTERVAL_MINUTES = 5  # интервал в минутах
MAX_PARALLEL_REQUESTS = 10  # максимальное количество параллельных запросов


async def handle_order(order_id, http_session, semaphore):
    pass


async def process_orders(orders, conn, semaphore):
    async with ClientSession() as session:
        #tasks = [fetch_order_status(session, order_id, semaphore) for order_id in orders]
        #await asyncio.gather(*tasks, return_exceptions=True)
        pass
        # for task in asyncio.as_completed(tasks):
        #     order_id, new_status = await task
        #     if new_status:
        #         current_status = next(status for id_, status in pending_orders if id_ == order_id)
        #         if new_status != current_status:
        #             await update_order_status(conn, order_id, new_status)
        #             print(f"Updated order {order_id} status to {new_status}")


async def test_connection():
    conn = await asyncpg.connect(DATABASE_URL)
    print('Connection successful')
    await conn.close()

import asyncio
asyncio.run(test_connection())

async def main():
    conn = await asyncpg.connect(DATABASE_URL)
    semaphore = asyncio.Semaphore(MAX_PARALLEL_REQUESTS)

    try:
        while True:
            orders = await get_incomplete_orders_ids(conn)
            await process_orders(orders, conn, semaphore)
            await asyncio.sleep(CHECK_INTERVAL_MINUTES * 60)
    finally:
        await conn.close()


if __name__ == "__main__":
    asyncio.run(main())
