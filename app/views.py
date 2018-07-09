from flask import render_template
from app import app
from app.models import Product, Category


@app.route('/')
@app.route('/main/')
def main():
    return render_template('main.html', title='Главная')


@app.route('/products/')
def products_list():
    prod_set = list(Product.query.all())
    return render_template('products_list.html', products=prod_set)


@app.route('/products/<product_id>')
def product(product_id):
    prod = None
    return render_template('product_item.html', prod=prod)
