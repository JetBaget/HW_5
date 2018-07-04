from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views, models

admin = Admin(app, name='flask_shop', template_mode='bootstrap3')
admin.add_view(ModelView(models.Category, db.session))
admin.add_view(ModelView(models.Product, db.session))
