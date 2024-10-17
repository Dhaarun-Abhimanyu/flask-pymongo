# **Flask with MongoDB (PyMongo) - Step-by-Step Guide**

This guide will walk you through setting up a basic Flask application with MongoDB (using MongoDB Atlas) and PyMongo, following a structured and modular approach.

---

## **1. Project Setup**

### **Step 1: Create the Project Directory**

```bash
mkdir flask_pymongo_app
cd flask_pymongo_app
```

### **Step 2: Setup Python Virtual Environment**

Set up a virtual environment to isolate your project dependencies.

```bash
# Create a virtual environment
python -m venv venv
```

Activate the virtual environment:

```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### **Step 3: Install Dependencies**

Install Flask, PyMongo, and other necessary libraries by creating a requirements.txt file.

```bash
# Create requirements.txt
touch requirements.txt
```

Add the following lines to requirements.txt:

```
Flask==2.3.2
pymongo==4.7.0
python-dotenv==1.0.0
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## **2. Project Structure**

Create a clean project structure to keep the code modular.

```
flask_pymongo_app/
│
├── .env                 # Environment variables (MongoDB URI)
├── app.py               # Main Flask application
├── config.py            # Configuration file for MongoDB URI
├── requirements.txt     # Python dependencies
├── routes/              # Folder for route files
│   ├── user_routes.py   # User-related routes
├── models/              # Folder for MongoDB models
│   └── user_model.py    # Model for user data
└── venv/                # Virtual environment
```

## **3. Environment Variables**

### **Step 1: Create the .env File**

Create a .env file to store your MongoDB connection string securely.

```bash
# Create .env file
touch .env
```

Add your MongoDB URI to the .env file:

```
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority
```

## **4. Application Code**

### **Step 1: Create the config.py File**

Create a config.py file for the configuration settings.

```python
# config.py

import os

class Config:
    MONGO_URI = os.getenv("MONGO_URI")
```

### **Step 2: Create the models/user_model.py File**

Create the user model to interact with MongoDB.

```python
# models/user_model.py

from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGO_URI)
db = client['your_database_name']

class UserModel:
    @staticmethod
    def create_user(user_data):
        return db.users.insert_one(user_data)

    @staticmethod
    def get_all_users():
        return list(db.users.find())
```

### **Step 3: Create the routes/user_routes.py File**

Define the user-related routes.

```python
# routes/user_routes.py

from flask import Blueprint, request, jsonify
from models.user_model import UserModel

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users', methods=['GET'])
def get_users():
    users = UserModel.get_all_users()
    return jsonify(users)

@user_routes.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    user_id = UserModel.create_user(user_data)
    return jsonify({"id": str(user_id.inserted_id)}), 201
```

### **Step 4: Create the app.py File**

Set up the main Flask application.

```python
# app.py

from flask import Flask
from dotenv import load_dotenv
from config import Config
from routes.user_routes import user_routes

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(user_routes)

if __name__ == '__main__':
    app.run(debug=True)
```

## **5. Running the Application**

### **Step 1: Run the Flask Application**

```bash
python app.py
```

### **Step 2: Access the API**

GET Request: `http://127.0.0.1:5000/users`

POST Request: `http://127.0.0.1:5000/users` with JSON body:

```json
{
    "name": "John Doe",
    "email": "john@example.com"
}
```

## **Conclusion**

You now have a basic Flask application connected to MongoDB using PyMongo. This structure can be further expanded with more models and routes as needed.