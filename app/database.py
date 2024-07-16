from pymongo import MongoClient
from dotenv import load_dotenv
import os 

load_dotenv()

def createConnection():
    protocol, id, pw, url = os.getenv('DB_PROTOCOL'), os.getenv('DB_ID'), os.getenv('DB_PW'), os.getenv('DB_URL')
    client = MongoClient(f"{protocol}://{id}:{pw}@{url}")
    db = client['para4']
    print('Database Connected!')
    return db

db = createConnection()

