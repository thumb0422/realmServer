from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from order.orderView import order

app = Flask(__name__)
app.config.from_object('mysqlConfig')
db = SQLAlchemy(app)

app.register_blueprint(order,url_prefix='/order')


if __name__ == '__main__':
    app.run(debug=True)
