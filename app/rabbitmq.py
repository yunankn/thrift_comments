import asyncio
import json
import traceback
from asyncio import AbstractEventLoop
from aio_pika.abc import AbstractRobustConnection, AbstractRobustChannel, AbstractQueue
from aio_pika import connect_robust, IncomingMessage, Message

from app.settings import settings

channel: AbstractRobustChannel = None

comment_created_queue: AbstractQueue = None
comment_rating_changed_queue: AbstractQueue = None


async def send_comment_created(data):
    await channel.default_exchange.publish(Message(bytes(data, 'utf-8')), routing_key='vodolazova_comment_created_queue')


async def send_comment_rating_changed(data):
    await channel.default_exchange.publish(Message(bytes(data, 'utf-8')), routing_key='vodolazova_comment_rating_changed_queue')


async def init_rabbit_mq(loop: AbstractEventLoop) -> AbstractRobustConnection:
    global channel
    global comment_created_queue
    global comment_rating_changed_queue
    print("Starting RabbitMQ")
    await asyncio.sleep(6)

    connection = await connect_robust(settings.amqp_url, loop=loop)
    channel = await connection.channel()

    comment_created_queue = await channel.get_queue('vodolazova_comment_created_queue')
    comment_rating_changed_queue = await channel.get_queue('vodolazova_comment_rating_changed_queue')

    print('Started RabbitMQ publishing...')

    return connection
