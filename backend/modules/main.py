from flask import Blueprint,request,jsonify
import base64

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return 'Hello, World!'

@main_bp.route("/photo",methods=["POST"])
def photo():
    photo = request.files["images"]
    image_string = str(base64.b64encode(photo.read()))
    return jsonify({"Responce":"OK","barcodeNumber":"111","Name":"Энергос","Cost":"90", "Shop":"Магнит","Date":"2022-07-10"})

