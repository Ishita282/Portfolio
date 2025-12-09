from flask import Blueprint, request, jsonify
from database.db import db, Comment

comment_bp = Blueprint("comment_bp", __name__)

@comment_bp.route("/comments", methods=["POST"])
def add_comment():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    if not name or not email or not message:
        return jsonify({"error": "All fields are required"}), 400

    new_comment = Comment(name=name, email=email, message=message)
    db.session.add(new_comment)
    db.session.commit()

    return jsonify({"message": "Comment added successfully!"})
