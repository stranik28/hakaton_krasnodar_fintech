from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/verify', methods=['POST'])
def auth():
    login = request.args.get('login')
    password = request.args.get('password')
    if login == 'admin' and password == 'admin':
        return jsonify({'token': 'admin'})
    elif login == 'user' and password == 'user':
        return jsonify({'token': 'user'})
    elif login == 'shop' and password == 'shop':
        return jsonify({'token': 'shop'})
    else:
        return jsonify({'token': 'access_denyed'})