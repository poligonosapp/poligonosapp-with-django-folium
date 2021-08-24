# https://docs.mongodb.com/drivers/motor/#connect-to-mongodb-atlas

import asyncio
import motor.motor_asyncio

async def get_server_info():

    # replace this with your MongoDB connection string
    conn_str = "<your MongoDB Atlas connection string>"

    # set a 5-second connection timeout
    client = motor.motor_asyncio.AsyncIOMotorClient(conn_str, serverSelectionTimeoutMS=5000)

    try:
        print(await client.server_info())
    except Exception:
        print("Unable to connect to the server.")

loop = asyncio.get_event_loop()
loop.run_until_complete(get_server_info())