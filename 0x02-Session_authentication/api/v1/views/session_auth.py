#!/usr/bin/env python3
""" Module of session auth views
"""

from flask import jsonify, abort, request
from api.v1.views import app_views
import os


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def login():
    """Login a user"""
    email = request.form.get("email")
    if not email:
        return jsonify({"error": "email missing"}), 400
    password = request.form.get("password")
    if not password:
        return jsonify({"error": "password missing"}), 400
    from models.user import User

    user_instance = User.search({"email": email})

    if not user_instance:
        return jsonify({"error": "no user found for this email"}), 404
    if not user_instance[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth

    session_id = auth.create_session(user_instance[0].id)
    user_dict = user_instance[0].to_json()
    response_obj = jsonify(user_dict)
    SESSION_NAME = os.getenv("SESSION_NAME")
    response_obj.set_cookie(SESSION_NAME, session_id)
    return response_obj


@app_views.route("/auth_session/logout",
                 methods=["DELETE"], strict_slashes=False)
def delete():
    from api.v1.app import auth

    destroy = auth.destroy_session(request)
    if destroy is False:
        abort(404)
    return jsonify({}), 200
