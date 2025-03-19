from pymongo import MongoClient
import random
import datetime

# Connect to MongoDB
client = MongoClient("mongodb+srv://yanie:qM0somsYwQXQEM9P@cluster0.qarpj.mongodb.net/?retryWrites=true&w=majority&tls=true")
db = client["trashTalk"]
collection = db["gasRecords"]

# Generate 100 random gas sensor readings
sensor_data = []
start_time = datetime.datetime(2025, 2, 1, 0, 0, 0)

for i in range(10000):
    data = {
        "timestamp": start_time + datetime.timedelta(minutes=i),  # Increments every hour
        "LPG_ppm": random.randint(0, 250),
        "Methane_ppm": random.randint(0, 250),
        "Hydrogen_ppm": random.randint(0, 250),
        "Smoke_ppm": random.randint(0, 250),
        "CO_ppm": random.randint(0, 250),
        "Temperature_C": round(random.uniform(0, 50.0), 1),
        "Humidity_percent": random.randint(0, 100),
    }
    sensor_data.append(data)

# Insert into MongoDB
collection.insert_many(sensor_data)
print("10000 sample gas sensor entries inserted successfully!")
