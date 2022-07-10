from flask import Blueprint, request, jsonify
from app.extension import db

cashback_bp = Blueprint('cashback', __name__)

@cashback_bp.route('/cash_back', methods=['GET'])
def get_cashback():
    category = request.args.get('category')
    coursor = db.connection.cursor()
    coursor.execute(f"SELECT * FROM `Shop` WHERE `cash_back` != 0 ")
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