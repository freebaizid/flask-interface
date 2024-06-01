from app import admin
from flask_admin.contrib.sqla import ModelView
from app import db
from .models import User, Post

def create_admin_views():

    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Post, db.session))
