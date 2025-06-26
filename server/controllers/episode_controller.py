from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from server.models.episode import Episode
from server.extentions import db


episode_controller = Blueprint('episode_controller', __name__)


@episode_controller.route('/episodes', methods=['GET'])
def list_episodes():
    episodes = Episode.query.all()
    result = [e.to_dict() for e in episodes] 
    return jsonify(result), 200

@episode_controller.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404

    db.session.delete(episode)
    db.session.commit()
    return jsonify({"message": "Episode deleted"}), 200
