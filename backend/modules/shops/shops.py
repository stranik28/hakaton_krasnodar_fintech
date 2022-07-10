import json
from flask import Blueprint, jsonify
from flask import request, jsonify
from app.extension import db
import json

shops_bp = Blueprint('shops', __name__)

@shops_bp.route('/')
def shops():
    cursor = db.connection.cursor()
    name = request.args.get('name')
    cursor.execute(" SELECT * FROM Shop WHERE name LIKE '%"+name+"%' ;")
    data = cursor.fetchall()
    answ = []
    for i in data:
        dict = {}
        dict['id'] = i[0]
        dict['name'] = i[1]
        dict['category'] = i[2]
        dict['cash_back'] = i[3]
        dict['rating'] = i[4]
        dict['location'] = i[5]
        dict['retail_id'] = i[6]
        answ.append(dict)
    return jsonify(answ)