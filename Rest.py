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