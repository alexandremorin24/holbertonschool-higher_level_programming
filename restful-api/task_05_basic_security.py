#!/usr/bin/python3
"""
API security implementation with Basic Authentication and JWT Authentication.
Background: API security is of paramount importance, especially when the API is
exposed to the wider internet.
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = ("super-secret-key")
jwt = JWTManager(app)
auth = HTTPBasicAuth()


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


@auth.verify_password
def verify_password(username, password):
    """Verify username and password for basic auth."""
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user
    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Return access message for basic auth."""
    return "Basic Auth: Access Granted", 200


@app.route("/login", methods=["POST"])
def login():
    """Handle user login and return JWT token."""
    data = request.get_json()

    username = data["username"]
    password = data["password"]

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity={"username": username,
                                                 "role": user["role"]})
    return jsonify({"access_token": access_token}), 200


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Return access message for JWT auth."""
    return "JWT Auth: Access Granted", 200


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Handle admin-only access."""
    current_user = get_jwt_identity()
    user_role = current_user["role"]
    if user_role != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted", 200


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
    """Handle fresh token requirement."""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
