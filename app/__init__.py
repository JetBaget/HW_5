from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys
sys.path.append('/root/work_venv/Otus/DZ_5/HW_5')

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, forms
