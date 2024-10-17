import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)
db = client['test']
users_collection = db['users']

# Create operation: Insert a new user
def create_user():
    user_data = {
        "name": "darshan",
        "email": "huh",
        "age": 28
    }
    result = users_collection.insert_one(user_data)
    print(f"User created with id: {result.inserted_id}")

# Read operation: Fetch all users
def read_users():
    users = users_collection.find()
    for user in users:
        print(user)

# Call the functions
create_user()
read_users()   # To read all users

# Close the connection
client.close()