from pymongo import MongoClient

client = MongoClient("mongodb+srv://yanie:qM0somsYwQXQEM9P@cluster0.qarpj.mongodb.net/?retryWrites=true&w=majority&tls=true")
db = client["trashTalk"]
users_collection = db["User"]
gas_collection = db["gasRecords"]

