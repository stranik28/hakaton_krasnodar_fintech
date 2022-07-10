from random import randint
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
# from app.extenstion import db
import ast
# print(db)
ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
       11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def recs_by_categories(data, user):
    # print(db)
    # # working with DB
    # # creating database cursor
    # cursor = db.connection.cursor()
    # # selecting userid, shopname, ProductName and Product cost
    # data = {'UserId':[], 'ProductCost':[], 'MCC':[]}
    # cursor.execute('''SELECT * FROM user''')
    # data = cursor.fetchall()

    # as output we get python dict called data
    # data = test_insert(data)
    # datas = pd.read_csv("src/data/sales.csv",encoding = "utf-16le")
    # converting into dataframe
    dictofshops = {0: ['STEAM', 5816],
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
                   17: ['DODO', 5814],
                   16: ['DODO', 5814]}
    print(data.keys())
    with open('teqt.txt', 'w') as t:
        t.write(str(data['ShopId']))
    for i, id in enumerate(data['ShopId']):
        
        print(data['ShopId'].keys()[i])
        # print(id)
        data['ShopId'][i] = dictofshops[i][1]
        # print(data['ShopId'][i])


    datas = pd.DataFrame(data)
    table1 = datas.groupby(['UserId', 'ShopId']).mean()['ProductCost']
    table1 = table1.to_frame()
    # new_data = datas.drop(['ProductName',"MCC"], axis = 1, inplace = False)
    new_data = pd.crosstab(
        datas['UserId'], datas['ShopId'], values=datas['ProductCost'], aggfunc='mean')
    new_data.fillna(0, inplace = True)
    csr_data = csr_matrix(new_data.values)
    knn = NearestNeighbors(metric = 'cosine', algorithm = 'brute', n_neighbors = 20, n_jobs = -1)
    knn.fit(csr_data)
    recommendations = 20
    distances, indices = knn.kneighbors(csr_data[user],n_neighbors = recommendations + 1)
    distances = distances[0][1:]
    indices = indices[0][1:]
    # print(distances)
    print(indices)
    
def test_insert(data):
    # merchants = ['Магнит',"Пятёрочка","Петшоп","Перекрёсток","Стим","Шейн","Алиекспресс","Икея","Булочная17","Булочная54","Булочная32","Булочная4","Булочная13","Булочная12","Булочная75","Булочная6","Булочная5",]
    for i in range(0,100):
        data['UserId'].append(i)
        data['ProductCost'].append(randint(100,5000))
        data['MCC'].append(randint(3000,8000))
    return data


def genCache():
    with open('modules/neuron/recs_categories/categories.txt', 'r') as textDict:
        dict = textDict.read()
        dict = ast.literal_eval(dict)
        print(type(dict))
    print(len(ids))
    for id in ids:
        path = f'modules/neuron/recs_categories/cache/{id}.txt'
        writeDict = recs_by_categories(dict, id)
        with open(path, 'w') as output:
            output.write(str(writeDict))


genCache()
