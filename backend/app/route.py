from flask import Blueprint
from modules.auth.auth import auth_bp
from modules.main import main_bp
from modules.category.category import category_bp
from modules.cashback.cashback import cashback_bp
from modules.recommendations.recommendations import recommendations_bp
from modules.shops.shops import shops_bp
from modules.profile.get_profile import get_profile_bp


def route(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(category_bp, url_prefix='/get_stores')
    app.register_blueprint(cashback_bp, url_prefix='/get_stores')
    app.register_blueprint(recommendations_bp, url_prefix="/recs")
    app.register_blueprint(shops_bp, url_prefix="/search")
    app.register_blueprint(get_profile_bp, url_prefix="/get_profile")
    app.register_blueprint(main_bp)
    return app