from crypt import methods
from flask import Blueprint, request, jsonify
from app.extension import db

category_bp = Blueprint('category', __name__)

@category_bp.route('/category', methods=['GET'])
def get_list():
    category = request.args.get('category')
    coursor = db.connection.cursor()
    coursor.execute(f"SELECT * FROM `Shop` WHERE `category` = '{category}'")
    data = coursor.fetchall()
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

