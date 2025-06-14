from flask import Blueprint, request, make_response
from models import db, User

user_bp = Blueprint('user_pb', __name__)

@user_bp.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        user_list = [user.to_dict() for user in User.query.all()]

        return make_response(user_list, 200)