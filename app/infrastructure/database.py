from pymongo import MongoClient
import os

client = MongoClient(os.environ.get("MONGO_URI"))
db = client[os.environ.get("DB_CLIENT")]
users_collection = db["User"]
gas_collection = db["gasRecords"]

