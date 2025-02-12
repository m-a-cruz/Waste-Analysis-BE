# from pymongo import MongoClient
# import random
# import datetime

# # Connect to MongoDB
# client = MongoClient("mongodb+srv://yanie:qM0somsYwQXQEM9P@cluster0.qarpj.mongodb.net/?retryWrites=true&w=majority&tls=true")
# db = client["trashTalk"]
# collection = db["gasRecords"]

# # Generate 100 random gas sensor readings
# sensor_data = []
# start_time = datetime.datetime(2025, 2, 1, 0, 0, 0)

# for i in range(100):
#     data = {
#         "timestamp": start_time + datetime.timedelta(hours=i),  # Increments every hour
#         "LPG_ppm": random.randint(200, 250),
#         "Methane_ppm": random.randint(150, 200),
#         "Hydrogen_ppm": random.randint(100, 150),
#         "Smoke_ppm": random.randint(50, 80),
#         "CO_ppm": random.randint(10, 20),
#         "Temperature_C": round(random.uniform(24.5, 30.0), 1),
#         "Humidity_percent": random.randint(40, 70),
#     }
#     sensor_data.append(data)

# # Insert into MongoDB
# collection.insert_many(sensor_data)
# print("100 sample gas sensor entries inserted successfully!")
