from flask import Blueprint, request, jsonify
from models.user_model import create_user, get_all_users, delete_user_by_name

# Create a blueprint for user routes
user_bp = Blueprint('user_routes', __name__)

# Route to create a user
@user_bp.route('/', methods=['POST'])
def add_user():
    data = request.json
    if data:
        result = create_user(data)
        return jsonify({'message': 'User created successfully!', 'id': str(result.inserted_id)}), 201
    return jsonify({'error': 'Invalid data'}), 400

# Route to get all users
@user_bp.route('/', methods=['GET'])
def get_users():
    users = get_all_users()
    return jsonify(users), 200

# Route to delete a user by name
@user_bp.route('/<name>', methods=['DELETE'])
def delete_user(name):
    result = delete_user_by_name(name)
    if result.deleted_count > 0:
        return jsonify({'message': f'User {name} deleted successfully'}), 200
    return jsonify({'error': 'User not found'}), 404