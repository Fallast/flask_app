from malabar import db, login_manager
from flask_login import UserMixin
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	__tablename__ = "user"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(40), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	# TODO:
		# relacion one-to-many con productos
	chart_products = db.relationship("Chart_products")
	bought_products = db.relationship("Bought_products")
	shipped_products = db.relationship("Shipped_products")

	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.password}')"

class Chart_products(db.Model):
	__tablename__ = "chart_products"
	id = db.Column(db.Integer, primary_key=True)
	user_id = Column(Integer, db.ForeignKey("user.id"))
	product = db.relationship("Product")
	quantity = db.Column(db.Integer)

class Bought_products(db.Model):
	__tablename__ = "bought_products"
	id = db.Column(db.Integer, primary_key=True)
	user_id = Column(Integer, db.ForeignKey("user.id"))
	product = db.relationship("Product")
	quantity = db.Column(db.Integer)

class Shipped_products(db.Model):
	__tablename__ = "shipped_products"
	id = db.Column(db.Integer, primary_key=True)
	user_id = Column(Integer, db.ForeignKey("user.id"))
	product = db.relationship("Product")
	quantity = db.Column(db.Integer)

# TODO:
# ruido con ForeignKey, estudiar many to many , dibujar
class Product(db.Model):
	__tablename__ = "product"
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(60), unique=True, nullable=False)
	price = db.Column(db.String(5), nullable=False)
	categories = db.Column(db.String(100), nullable=False)
	descriptions = db.Column(db.String(100), nullable=True)
	quantity = db.Column(db.Integer)
	thumbnail = db.Column(db.String(30), nullable=False)

	def __repr__(self):
		return f"Product('{self.id}', '{self.title}', '{self.price}', '{self.categories}', '{self.descriptions}', '{self.quantity}', '{self.thumbnail}')"

class ProductSchema(SQLAlchemyAutoSchema):
	class Meta:
		model = Product
		load_instance = True

