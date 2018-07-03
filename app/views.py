from flask import render_template
from app import app


@app.route('/')
@app.route('/main/')
def main():
    return render_template('index.html', title='Главная')


@app.route('/products/', methods=['GET', 'POST'])
def product():
    prod_set = [{'header': 'IPhone 7 (100500Гб, полный фарш)',
                 'params': ['Объем памяти: 64Гб', 'Цвет: Черный', 'Диагональ экрана: 5.5`'],
                 'img_path': '/static/img/iphone7.jpg',
                 'desc': 'Некуда девать лишние деньги? Тогда это лучший выбор!'},
                {'header': 'Macbook Air 2018 (16Гб оперативы)',
                 'params': ['Объем оперативной памяти: 16Гб', 'Жёсткий диск: 500Гб', 'Цвет: Серебристый', 'Диагональ экрана: 17`'],
                 'img_path': '/static/img/macbook.jpg',
                 'desc': 'Охурменный ноутбук за нехилое баблище'}]
    return render_template('item.html', products=prod_set)

