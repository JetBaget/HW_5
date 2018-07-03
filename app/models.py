from app import db

ROLE_USER = 0
ROLE_ADMIN = 1


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(), index=True)
    params = db.Column(db.String())
    img_path = db.Column(db.String(64), index=True, unique=True)
