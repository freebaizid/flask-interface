from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'
admin = Admin(template_mode='bootstrap3')

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)

    with app.app_context():
        # Include our Routes
        from . import routes, auth_routes
        from .admin import create_admin_views
        
        # Register Blueprints
        app.register_blueprint(routes.bp)
        app.register_blueprint(auth_routes.bp)

        # Create admin views
        create_admin_views()

        db.create_all()

    return app