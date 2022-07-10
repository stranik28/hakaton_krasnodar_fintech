import json
from flask import Blueprint
from flask import request, jsonify
from app.extension import db
import json

get_profile_bp = Blueprint('get_profile', __name__)

@get_profile_bp.route('/')
def get_profile():
    cursor = db.connection.cursor()
    id = request.args.get('id')
    cursor.execute('''SELECT * FROM user WHERE id = %s ;''',(id))
    data = cursor.fetchall()
    answ = []
    for i in data:
        dict = {}
        dict['id'] = i[0]
        dict['name'] = i[1]
        dict['exp'] = i[2]
        dict['leag_id'] = i[3]
        answ.append(dict)
    return jsonify(answ)
