from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models.appearance import Appearance
from server.extentions import db


appearance_controller = Blueprint('appearance_controller', __name__)

@appearance_controller.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    try:
        appearance = Appearance(
            rating=data['rating'],
            guest_id=data['guest_id'],
            episode_id=data['episode_id']
        )
        db.session.add(appearance)
        db.session.commit()
        return jsonify({"message": "Appearance created"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
