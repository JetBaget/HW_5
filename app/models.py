from app import db
from sqlalchemy.dialects import postgresql

ROLE_USER = 0
ROLE_ADMIN = 1


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<Category %r>' % self.name


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    title = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(), index=True)
    params = db.Column(postgresql.JSONB(astext_type=False), index=True)
    img_path = db.Column(db.String(64), index=True, unique=True)
    category = db.relationship('Category', backref=db.backref('product', lazy=True))

    def __repr__(self):
        return '<Post %r>' % self.title
