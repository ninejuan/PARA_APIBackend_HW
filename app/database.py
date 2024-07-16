from pymongo import MongoClient
from dotenv import load_dotenv
import os 

env = os.environ

def createConnection():
    client = MongoClient(f"{env.DB_PROTOCOL}://{env.DB_ID}:{env.DB_PW}@{env.DB_URL}")
    db = client['para4']
    print('Database Connected!')
    return db

