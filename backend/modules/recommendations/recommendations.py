from cgitb import text
import pandas as pd
from flask import Blueprint
from flask import request, jsonify
import requests
from app.extenstion import db
# from modules.neuron.recs_shops.recs_shops import recs_by_shops

import ast


recommendations_bp = Blueprint('recommendations', __name__)

@recommendations_bp.route('/shops')
def recsShops():
    user_id = request.args.get('id')
    cursor = db.connection.cursor()
    
    data = {'UserId':[], 'ProductCost':[], 'MerchantName':[]}
    cursor = db.connection.cursor()
    cursor.execute("select database();")

    cursor.execute("SELECT (user_id) FROM Receipt;")
    userColumn = cursor.fetchall()

    cursor.execute("SELECT (ammount) FROM Receipt;")
    productCostColumn = cursor.fetchall()

    cursor.execute("SELECT (shop_id) FROM Receipt;")
    shopIdsColumn = cursor.fetchall()

    userColumn = list(userColumn)
    productCostColumn = list(productCostColumn)
    shopIdsColumn = list(shopIdsColumn)

    dictofshops = {
    0: ['STEAM',5816], 
    1: ['Пятёрочка',5441], 
    2: ['Магнит',5441], 
    3: ['apteka.ru',5912], 
    4: ['GS auto',7538], 
    5: ['Перекресток',5441], 
    6: ['ikea.com',5712], 
    7: ['PetShop.ru',5995], 
    8: ['shein.com',5691], 
    9: ['Газпром',5541], 
    10: ['OSAKA',5814], 
    11: ['MACDONALDS',5814], 
    12: ['Epic Games Store',5816], 
    13: ['DNS',5732], 
    14: ['ActividionBlizzard',5816], 
    15: ['DODO',5814],
        16: ['DODO', 5814],

    }
    # print(userColumn)

    for i in range(0,len(userColumn)):
        # print(userColumn[i])
        if(userColumn[i]!='()'):
            # print(str(userColumn[i])[1:-2])
            userColumn[i] = int(str(userColumn[i])[1:-2])
        else:
            userColumn[i] = 0
            print('0')
        
        if(productCostColumn[i]!='()'):
            # print(str(userColumn[i])[1:-2])
            productCostColumn[i] = float(str(productCostColumn[i])[1:-2])
        else:
            productCostColumn[i] = 0
            print('0')
        
        if(shopIdsColumn[i]!='()'):
            # print(str(userColumn[i])[1:-2])
            shopIdsColumn[i] = dictofshops[int(str(shopIdsColumn[i])[1:-2])][0]
        else:
            shopIdsColumn[i] = 0
            print('0')

    data = {'UserId':userColumn, 'ProductCost':productCostColumn, 'MerchantName':shopIdsColumn}
    datas = pd.DataFrame(data)
    # print(data)
    with open(f'modules/neuron/recs_shops/cache/{user_id}.txt') as cachedDict:
        outDict = {}
        cachedDict = cachedDict.read()
        cachedDict = ast.literal_eval(cachedDict)
        print(cachedDict['indices'])
        for i, id in enumerate(cachedDict['indices'], 0):
            print(i)
            cursor.execute(f'SELECT shop_id, MAX(ammount) AS Макс FROM Receipt WHERE user_id={id} GROUP BY shop_id ORDER BY Макс DESC;')
            maxShop = [item[0] for item in cursor.fetchall()]
            print(maxShop)
            outDict[i] = {'name': dictofshops[maxShop[0]][0]}

    return jsonify(outDict)

@recommendations_bp.route('/user_rec_shops')
def usRecShops():
    user_id = request.args.get('id')
    cursor = db.connection.cursor()

    data = {'UserId': [], 'ProductCost': [], 'MerchantName': []}
    cursor = db.connection.cursor()
    cursor.execute("select database();")

    cursor.execute("SELECT (user_id) FROM Receipt;")
    userColumn = cursor.fetchall()

    cursor.execute("SELECT (ammount) FROM Receipt;")
    productCostColumn = cursor.fetchall()

    cursor.execute("SELECT (shop_id) FROM Receipt;")
    shopIdsColumn = cursor.fetchall()

    userColumn = list(userColumn)
    productCostColumn = list(productCostColumn)
    shopIdsColumn = list(shopIdsColumn)

    dictofshops = {
        0: ['STEAM', 5816],
        1: ['Пятёрочка', 5441],
        2: ['Магнит', 5441],
        3: ['apteka.ru', 5912],
        4: ['GS auto', 7538],
        5: ['Перекресток', 5441],
        6: ['ikea.com', 5712],
        7: ['PetShop.ru', 5995],
        8: ['shein.com', 5691],
        9: ['Газпром', 5541],
        10: ['OSAKA', 5814],
        11: ['MACDONALDS', 5814],
        12: ['Epic Games Store', 5816],
        13: ['DNS', 5732],
        14: ['ActividionBlizzard', 5816],
        15: ['DODO', 5814],
        16: ['DODO', 5814],

    }
    # print(userColumn)

    for i in range(0, len(userColumn)):
        # print(userColumn[i])
        if(userColumn[i] != '()'):
            # print(str(userColumn[i])[1:-2])
            userColumn[i] = int(str(userColumn[i])[1:-2])
        else:
            userColumn[i] = 0
            print('0')

        if(productCostColumn[i] != '()'):
            # print(str(userColumn[i])[1:-2])
            productCostColumn[i] = float(str(productCostColumn[i])[1:-2])
        else:
            productCostColumn[i] = 0
            print('0')

        if(shopIdsColumn[i] != '()'):
            # print(str(userColumn[i])[1:-2])
            shopIdsColumn[i] = dictofshops[int(str(shopIdsColumn[i])[1:-2])][0]
        else:
            shopIdsColumn[i] = 0
            print('0')

    data = {'UserId': userColumn, 'ProductCost': productCostColumn,
            'MerchantName': shopIdsColumn}
    datas = pd.DataFrame(data)
    # print(data)
    with open(f'modules/neuron/recs_shops/cache/{user_id}.txt') as cachedDict:
        outDict = {}
        cachedDict = cachedDict.read()
        cachedDict = ast.literal_eval(cachedDict)
        print(cachedDict['indices'])
        for i, id in enumerate(cachedDict['indices'], 0):
            print(i)
            cursor.execute(
                f'SELECT shop_id, MAX(ammount) AS Макс FROM Receipt WHERE user_id={id} GROUP BY shop_id ORDER BY Макс DESC;')
            maxShop = [item[0] for item in cursor.fetchall()]
            print(maxShop)
            outDict[i] = {'name': dictofshops[maxShop[3]][0]}

    return jsonify(outDict)

@recommendations_bp.route('/products')
def recsProducts():
    outDict = {}

    user_id = request.args.get('id')
    cursor = db.connection.cursor()

    data = {'UserId': [], 'ProductCost': [], 'ProductName': []}
    cursor = db.connection.cursor()
    cursor.execute("select database();")

    cursor.execute("SELECT (user_id) FROM Receipt;")
    userColumn = cursor.fetchall()

    cursor.execute("SELECT (ammount) FROM Receipt;")
    productCostColumn = cursor.fetchall()

    cursor.execute("SELECT (product) FROM Receipt;")
    shopIdsColumn = cursor.fetchall()

    userColumn = list(userColumn)
    productCostColumn = list(productCostColumn)
    shopIdsColumn = list(shopIdsColumn)

    with open(f'modules/neuron/recs_products/cache/{user_id}.txt') as cachedDict:
        cachedDict = cachedDict.read()
        cachedDict = ast.literal_eval(cachedDict)
        print(cachedDict['indices'])
        for i, id in enumerate(cachedDict['indices'], 0):
            # print(i)
            cursor.execute(
                f'SELECT product, MAX(ammount) AS Макс FROM Receipt WHERE user_id={id} GROUP BY product ORDER BY Макс DESC;')
            maxProducts = [item[0] for item in cursor.fetchall()]
            # print(maxProducts)
            outDict[i] = {'name': maxProducts[2]}
        
        # maxProducts = [item[0] for item in cursor.fetchall()]
        # print(maxProducts)
        # for i, product in enumerate(maxProducts, 0):
        #     print(i)
        #     outDict[i] = product

    return jsonify(outDict)

@recommendations_bp.route('/average_products')
def average_products():
    outDict = {}

    user_id = request.args.get('id')
    cursor = db.connection.cursor()

    data = {'UserId': [], 'ProductCost': [], 'ProductName': []}
    cursor = db.connection.cursor()
    cursor.execute("select database();")

    cursor.execute("SELECT (user_id) FROM Receipt;")
    userColumn = cursor.fetchall()

    cursor.execute("SELECT (ammount) FROM Receipt;")
    productCostColumn = cursor.fetchall()

    cursor.execute("SELECT (product) FROM Receipt;")
    shopIdsColumn = cursor.fetchall()

    userColumn = list(userColumn)
    productCostColumn = list(productCostColumn)
    shopIdsColumn = list(shopIdsColumn)

    with open(f'modules/neuron/recs_products/cache/{user_id}.txt') as cachedDict:
        cachedDict = cachedDict.read()
        cachedDict = ast.literal_eval(cachedDict)
        print(cachedDict['indices'])
        for i, id in enumerate(cachedDict['indices'], 0):
            # print(i)
            cursor.execute(
                f'SELECT product, MAX(ammount) AS Макс FROM Receipt WHERE user_id={id} GROUP BY product ORDER BY Макс DESC;')
            maxProducts = [item[0] for item in cursor.fetchall()]
            # print(maxProducts)
            outDict[i] = {'name': maxProducts[3]}

        # maxProducts = [item[0] for item in cursor.fetchall()]
        # print(maxProducts)
        # for i, product in enumerate(maxProducts, 0):
        #     print(i)
        #     outDict[i] = product

    return jsonify(outDict)
