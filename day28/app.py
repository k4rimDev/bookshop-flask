from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@127.0.0.1:3306/book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


from extensions import *
from controllers import *
from models import *


if __name__ == '__main__':
    app.init_app(db)
    app.init_app(migrate)
    app.run(port=5000, debug = True)

