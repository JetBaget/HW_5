from app import db
import json

ROLE_USER = 0
ROLE_ADMIN = 1


class JsonEncodedDict(db.TypeDecorator):
    """Enables JSON storage by encoding and decoding on the fly."""
    impl = db.Text

    def process_bind_param(self, value, dialect):
        if value is None:
            return '{}'
        else:
            return json.dumps(value)

    def process_result_value(self, value, dialect):
        if value is None:
            return {}
        else:
            return json.loads(value)


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<Category %r>' % self.name


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    category = db.relationship('Category', backref=db.backref('product', lazy=True))
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    title = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(), index=True)
    params = db.Column(db.JSON(), index=True)
    img_path = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<Post %r>' % self.title
