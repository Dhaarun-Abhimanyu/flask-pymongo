from pymongo import MongoClient
from config import Config  # Import your configuration

# MongoDB connection using the MONGO_URI from Config
client = MongoClient(Config.MONGO_URI)
db = client['mydatabase']
collection = db['users']

def create_user(data):
    """Insert a new user into the database."""
    return collection.insert_one(data)

def get_all_users():
    """Fetch all users from the database."""
    users = list(collection.find({}))
    for user in users:
        user['_id'] = str(user['_id'])
    return users

def delete_user_by_name(name):
    """Delete a user by their name."""
    return collection.delete_one({"name": name})