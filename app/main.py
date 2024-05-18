import asyncio
from fastapi import FastAPI

from app import rabbitmq
from app.settings import settings
from app.endpoints.comments_router import comments_router


app = FastAPI(title='Comments Service')


@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(rabbitmq.init_rabbit_mq(loop))


app.include_router(comments_router, prefix='/api')
