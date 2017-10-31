from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from order.orderVC import OrderAction

app = Flask(__name__)
app.config.from_object('mysqlConfig')
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    action = OrderAction;
    return action.queryOrderByOrderId

if __name__ == '__main__':
    app.run(debug=True)
