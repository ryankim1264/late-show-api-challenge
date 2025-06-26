from flask import Blueprint, make_response
from server.models.guest import Guest

guest_controller = Blueprint('guest_controller', __name__)


@guest_controller.route('/guests', methods=['GET'])
def list_guests():
    guests = Guest.query.all()
    result = [g.to_dict() for g in guests] 
    return make_response(result,200)