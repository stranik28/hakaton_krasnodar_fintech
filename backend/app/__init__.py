from flask import Flask
from app.route import route
import os
from app.config import config, init_config
from app.extension import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def create_flask_app():
    route(app)
    path = os.environ.get('CONFIG_PATH') if os.environ.get(
        'CONFIG_PATH') else "./settings.ini"
    init_config(path)
    db.init_app(app)
    try:
        app.config.update(dict(
            MYSQL_HOST=str(config['MYSQL']['MYSQL_HOST']),
            MYSQL_USER=str(config['MYSQL']['MYSQL_USER']),
            MYSQL_PASSWORD=str(config['MYSQL']['MYSQL_PASSWORD']),
            MYSQL_DB=str(config['MYSQL']['MYSQL_DB'])
        ))
        print(f"\n\033[32m Сервер запустился с конфигом:\n\033[32m {path}\n")
    except KeyError:
        print(f"\033[31m Файл {path} не найден или неверный")
    return app
