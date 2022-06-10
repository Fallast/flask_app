from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = '73850c924bfa0ca5993272f5565c3ee7e5151d3c21c825d889038a7694bfd8d1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['RESIZE_URL'] = 'http://127.0.0.1:5000'
app.config['RESIZE_ROOT'] = '/home/batman/projects/full/malabar/malabar/static/product_pics'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from malabar import routes

import os
from os.path import *
from PIL import Image

# TODO: separar archivos en /product_pics agregar versiones de ellos de baja y
# maxima resolucion con pillow, probe con flask_resize y no anduvo nada

relative_path1 = "static/product_pics/"
relative_path2 = "static/product_pics_home/"
relative_path3 = "static/product_pics_cart/"
abs_product_pics_path = os.path.join(app.root_path, relative_path1)
abs_product_pics_home_path = os.path.join(app.root_path, relative_path2)
abs_product_pics_cart_path = os.path.join(app.root_path, relative_path3)
product_pics = [i for i in os.listdir(abs_product_pics_path)]
product_pics_home = [i for i in os.listdir(abs_product_pics_home_path)]
product_pics_cart = [i for i in os.listdir(abs_product_pics_cart_path)]
for i in product_pics:
    if(i not in product_pics_home):
        img = Image.open(abs_product_pics_path + i)
        img.thumbnail((500,500))
        img.save(abs_product_pics_home_path + i)
    if(i not in product_pics_cart):
        img = Image.open(abs_product_pics_path + i)
        img.thumbnail((100,100))
        img.save(abs_product_pics_cart_path + i)
