from malabar import db, login_manager
from flask_login import UserMixin
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(40), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	cart_products = db.relationship("Cart_product", backref="user")
	bought_products = db.relationship("Bought_product", backref="user")
	Shipping_products = db.relationship("Shipping_product", backref="user")
	shipped_products = db.relationship("Shipped_product", backref="user")

	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.password}')"

class Cart_product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
	prod_id = db.Column(db.Integer, db.ForeignKey("product.id"))
	prod = db.relationship("Product", back_populates="carts")
	quantity = db.Column(db.Integer)

class Bought_product(db.Model):
	__tablename__ = "bought_product"
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
	prod_id = db.Column(db.Integer, db.ForeignKey("product.id"))
	quantity = db.Column(db.Integer)

class Shipping_product(db.Model):
	__tablename__ = "shipping_product"
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
	prod_id = db.Column(db.Integer, db.ForeignKey("product.id"))
	quantity = db.Column(db.Integer)

class Shipped_product(db.Model):
	__tablename__ = "shipped_product"
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
	prod_id = db.Column(db.Integer, db.ForeignKey("product.id"))
	quantity = db.Column(db.Integer)

class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	carts = db.relationship("Cart_product", back_populates="prod")
	title = db.Column(db.String(60), unique=True, nullable=False)
	price = db.Column(db.String(5), nullable=False)
	categories = db.Column(db.String(100), nullable=False)
	descriptions = db.Column(db.String(100), nullable=True)
	quantity = db.Column(db.Integer)
	image = db.Column(db.String(30), nullable=False)

	def __repr__(self):
		return f"Product('{self.id}', '{self.title}', '{self.price}', '{self.categories}', '{self.descriptions}', '{self.quantity}', '{self.image}')"

class ProductSchema(SQLAlchemyAutoSchema):
	class Meta:
		model = Product
		load_instance = True

