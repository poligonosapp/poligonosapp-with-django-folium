# https://docs.mongodb.com/drivers/motor/#installation
# cloud mongodb https://docs.atlas.mongodb.com/troubleshoot-connection/

from github import Github

# First create a Github instance:

# using an access token
g = Github("repo-token")

# MONGODB_URL = Github("ream-secret")
# client = motor.motor_asyncio.AsyncIOMotorClient(os.environ[MONGODB_URL])

# def getMongoUrl() return g.get_user();

# client = pymongo.MongoClient("mongodb+srv://fail:<password>@cluster0.neyhi.gcp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# db = client.test

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
