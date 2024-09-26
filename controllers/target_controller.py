from returns.maybe import Nothing

from service import target_service
from repository import target_repository
from flask import Blueprint, jsonify

targets_blueprint = Blueprint("targets", __name__)

@targets_blueprint.route("/", methods=["GET"])
def index():
    try:
        targets = target_service.find_all_targets()
        return jsonify({'targets': targets}), 200
    except Exception as e:
        return jsonify({'error': repr(e)}), 500

@targets_blueprint.route("/<target_id>", methods=["GET"])
def target_by_id(target_id: int):
    try:
        maybe_target = target_repository.find_by_id(target_id)
        if maybe_target is Nothing:
            return jsonify({'error': 'Target not found!'}), 404
        target = maybe_target.unwrap()
        return jsonify({'target': target_service.target_to_dict(target)}), 200
    except Exception as e:
        return jsonify({'error': repr(e)}), 500