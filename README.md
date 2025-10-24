# 🌐 REST API with Flask

![Header](images/header.png)

---

## 📘 Project Overview

This project demonstrates how to build a **simple RESTful API** using **Flask**, a lightweight and flexible web framework in Python. The API provides basic CRUD (Create, Read, Update, Delete) operations for managing users stored in an **in-memory dictionary**.

The goal is to understand how REST APIs work and how to set up endpoints that handle different HTTP methods like **GET, POST, PUT, and DELETE**.

---

## 🎯 Objective

* To create a basic REST API using Flask.
* To define multiple endpoints for user management.
* To store user data in an **in-memory dictionary or list** instead of a database.

---

## 🛠️ Technologies Used

* **Python 3.x**
* **Flask** (for creating the REST API)
* **JSON** (for data exchange)

---

## 💻 Code Implementation

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {}

# Home route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask REST API!"}), 200

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# Get user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

# Add a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = len(users) + 1
    users[user_id] = {
        "id": user_id,
        "name": data.get("name"),
        "email": data.get("email")
    }
    return jsonify({"message": "User added successfully", "user": users[user_id]}), 201

# Update existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    users[user_id].update(data)
    return jsonify({"message": "User updated", "user": users[user_id]}), 200

# Delete user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    del users[user_id]
    return jsonify({"message": f"User {user_id} deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

---

## ⚙️ How It Works

1. Run the Flask app using `python app.py`.
2. Use **Postman** or **curl** to test different API endpoints:

   * `GET /users` → Retrieve all users.
   * `POST /users` → Add a new user.
   * `GET /users/<id>` → Retrieve specific user details.
   * `PUT /users/<id>` → Update an existing user.
   * `DELETE /users/<id>` → Remove a user.

---

## ✅ Results

* Successfully implemented a **working REST API** using Flask.
* Supports **CRUD operations** with user data stored in an in-memory structure.
* Easily extendable to include authentication or database integration.

---

## 🧑‍🏫 Author
**Prathamesh Sitaram Warak**  
B.E. Information Technology | Atharva College of Engineering  
Passionate about coding, cybersecurity,AI-ML and building real-world tech projects.
