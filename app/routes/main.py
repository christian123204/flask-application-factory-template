from flask import Blueprint, request

from ..extensions import db
from ..models.user import User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Index page'

@main.route('/user', methods=['GET'])
def get_user():
    id = request.args.get('id', None)

    if not id:
        return 404

    user = User.query.filter_by(id=id).first()

    if not user:
        return 404

    data = {
        'id': user.id,
        'name': user.name,
        'ags': user.age
    }

    return data


@main.route('/user', methods=['POST'])
def create_user():
    name = request.json.get('name', None)
    age = request.json.get('age', None)

    if not name or not age:
        return 400

    user = User(name=name, age=age)
    db.session.add(user)
    db.session.commit()

    return 'User added!'