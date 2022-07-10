import cv2
from pyzbar.pyzbar import decode

import numpy as np

from flask import Blueprint
from flask import request, jsonify

import base64

cap = cv2.VideoCapture(0)


barcode_bp = Blueprint('barcode_scanner', __name__)


@barcode_bp.route('/',methods=['GET', 'POST'])
def barcode_scanner():
    def barcode_scanner2(img_string):
        out_data = {}
        with open('64.txt','w') as sda:
            sda.write(img_string)
        nparr = np.fromstring(base64.b64decode(img_string), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        # print(img)
        print(nparr)
        barcodeData = decode(img)
        for barcode in barcodeData:
            barcodeNumber = barcode.data.decode('utf-8')
            if(barcodeNumber):
                barcodeNumber = int(barcodeNumber)
                print(barcodeNumber)
                if(barcodeNumber == 4600494694233):
                    out_data['Responce'] = 'OK'
                    out_data["barcodeNumber"] = barcodeNumber
                    out_data["Name"] = 'Энергетик Драйв'
                    out_data["Cost"] = '90р'
                    out_data["Shop"] = 'Магнит'
                    out_data["Date"] = '2022-07-10'
                if(barcodeNumber == 4610044160149):
                    out_data['Responce'] = 'OK'
                    out_data["barcodeNumber"] = barcodeNumber
                    out_data["Name"] = 'Вода Байкал'
                    out_data["Cost"] = '110р'
                    out_data["Shop"] = 'Табрис'
                    out_data["Date"] = '2022-07-10'
                if(barcodeNumber == 4600494692161):
                    out_data['Responce'] = 'OK'
                    out_data["barcodeNumber"] = barcodeNumber
                    out_data["Name"] = 'Энергетик Драйв'
                    out_data["Cost"] = '80р'
                    out_data["Shop"] = 'Магнит'
                    out_data["Date"] = '2022-07-10'
                if(barcodeNumber == 4600494698682):
                    out_data['Responce'] = 'OK'
                    out_data["barcodeNumber"] = barcodeNumber
                    out_data["Name"] = 'Энергетик Драйв'
                    out_data["Cost"] = '80р'
                    out_data["Shop"] = 'Магнит'
                    out_data["Date"] = '2022-07-10'
                else:
                    out_data['Responce'] = 'Not OK'
            else:
                out_data['Responce'] = 'Not OK'
            
            print(out_data)
            return(jsonify(out_data))
    
    photo = request.files["images"]
    image_string = str(base64.b64encode(photo.read()))

    # with open('base64.txt', 'r')as base:
    #     image_string = base.read()

    
    # print(image_string)
    barcode_scanner2(image_string)
    # barcode_scanner2(image_string)
    
