#!/usr/bin/python3
"""
Flask API with Basic Authentication and JWT Authentication.

This API provides:
- Basic authentication using `flask_httpauth`
- JWT authentication with role-based access control
- Protected routes requiring valid authentication
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = (
    "823033786d5b8496ddcd84a924895ae992310bb1eb3ca6ba95cff8557d2d6c82")

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# Basic Authentication


@auth.verify_password
def verify_password(username, password):
    """Verify username and password for basic auth."""
    if username in users:
        stored_password = users[username]["password"]
        if check_password_hash(stored_password, password):
            return username
    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Route accessible only with Basic Auth."""
    return jsonify({"message": "Basic Auth: Access Granted"})


# JWT Authentication
@app.route("/login", methods=["POST"])
def login():
    """Login route to obtain JWT token."""
    data = request.get_json()

    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Missing username or password"}), 400

    username = data["username"]
    password = data["password"]

    if (username not in users or
            not check_password_hash(users[username]["password"], password)):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity={"username": username, "role": users[username]["role"]})
    return jsonify({"access_token": access_token})


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Route accessible only with valid JWT token."""
    current_user = get_jwt_identity()
    return jsonify({"message": "JWT Auth: Access Granted"})


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Route accessible only with admin role."""
    current_user = get_jwt_identity()

    if current_user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"})


# 🔹 Gestion des erreurs JWT
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing JWT token."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid JWT token."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handle expired JWT token."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handle revoked JWT token."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handle when fresh token is required."""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run(debug=True)
