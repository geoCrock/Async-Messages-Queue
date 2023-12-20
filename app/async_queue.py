import aio_pika

from app.db import SessionLocal, TextTable
from config import RABBITMQ_URL
from xcount import count_x


# Asynchronous function to send a message
async def send_message(datetime: str, title: str, text: str):
    # Establishing a connection with RabbitMQ
    connection = await aio_pika.connect_robust(RABBITMQ_URL)

    # Creating a channel for data exchange with RabbitMQ
    channel = await connection.channel()

    # Set the queue name
    queue_name = "text"

    # We announce the queue
    await channel.declare_queue(queue_name)

    # Creating the body of the message
    message_body = text

    # Create a message object with the specified body and head
    message = aio_pika.Message(body=message_body.encode(), headers={'datetime': datetime, 'title': title})

    # Publish a message to the queue
    await channel.default_exchange.publish(message, routing_key=queue_name)

    # Closing the connection
    await connection.close()


async def receive_message():
    # Establishing a connection with RabbitMQ
    connection = await aio_pika.connect_robust(RABBITMQ_URL)

    # Creating a channel for data exchange with RabbitMQ
    channel = await connection.channel()

    # Set the queue name
    queue_name = "text"

    # We announce the queue
    queue = await channel.declare_queue(queue_name)

    # Callback function to process received messages
    async def callback(message: aio_pika.IncomingMessage):
        # We process the message asynchronously
        async with message.process():
            # Adding a message to the database
            title = message.headers.get("title", "")
            datetime = message.headers.get('datetime', '')
            x = await count_x(message.body.decode())
            db = SessionLocal()
            db_text = TextTable(datetime=datetime, title=title, x_avg_count_in_line=x)
            db.add(db_text)
            db.commit()
            db.refresh(db_text)
            db.close()

    # Set up a callback function to process messages from the queue
    await queue.consume(callback)
