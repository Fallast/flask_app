from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
import flask_resize

app = Flask(__name__)
app.config['SECRET_KEY'] = '73850c924bfa0ca5993272f5565c3ee7e5151d3c21c825d889038a7694bfd8d1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['RESIZE_URL'] = 'http://127.0.0.1:5000'
app.config['RESIZE_ROOT'] = '/home/batman/projects/full/malabar/malabar/static/product_pics'
db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
resize = flask_resize.Resize(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from malabar import routes

# TODO: separar archivos en /product_pics agregar versiones de ellos de baja y
# maxima resolucion con pillow, probe con flask_resize y no anduvo nada
