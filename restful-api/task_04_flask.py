#!/usr/bin/python3
"""Flask API for user management."""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}


@app.route("/")
def home():
    """Return a welcome message."""
    return jsonify({"message": "Welcome to the Flask API!"})


@app.route("/data")
def get_users():
    """Return a list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Return API status."""
    return jsonify({"status": "OK"})


@app.route("/users/<username>")
def get_user(username):
    """Return user details if found, otherwise return an error."""
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user if the username is provided in the request."""
    data = request.get_json()

    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run(debug=True)
