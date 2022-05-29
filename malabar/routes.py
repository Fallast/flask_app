import flask_resize
from PIL import Image
from malabar import (
        app,
        db,
        resize,
        bcrypt,
        ma
        )

from malabar.models import (
        User,
        Product,
        ProductSchema
        )

from flask import (
        render_template,
        url_for,
        flash,
        redirect,
        request,
        jsonify
        )

from malabar.forms import (
        RegistrationForm,
        LoginForm,
        ShippingForm,
        UpdateAccountForm
        )

from flask_login import (
        login_user,
        current_user,
        logout_user,
        login_required
        )

quantity = 6

# @app.route("/")
# @app.route("/home")
# def home():
    # query = Product.query.order_by(Product.id.desc()).all()
    # prod_schema = ProductSchema(many=True)
    # output = prod_schema.dump(query)
    # return render_template('home.html', title='Home', products_json=output)

@app.route("/")
@app.route("/home", methods=['GET','POST'])
def home():
    products = Product.query.order_by(Product.id.desc()).all()
    prod_schema = ProductSchema(many=True)
    categories = [x.categories for x in products]
    print(categories)
    return render_template('home.html', title='Home', products=products, categories=categories)

@app.route("/_search")
def search():
    search_str = request.args.get("s", '')
    query = Product.query.filter(Product.title.contains(search_str)).all()
    prod_schema = ProductSchema(many=True)
    output = prod_schema.dump(query)
    print(output)
    print()
    return ''



@app.route("/load")
def load():
    time.sleep(0.3)

    if request.args:
        counter = int(request.args.get("c"))

@app.route("/product/<item>")
def product(item):
    product = Product.query.filter_by(id=item).first()
    title = product.title
    price = product.price
    thumbnail = product.thumbnail
    quantity = product.quantity
    descriptions = product.descriptions
    return render_template('product.html', title=title, price=price,
            thumbnail=thumbnail, quantity=quantity, descriptions=descriptions)

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    print(a+b)
    return jsonify(results=a + b)

@app.route('/_str', methods=["GET","POST"])
def str():
    s = request.form.get('text', '')
    print(s)
    query = Product.query.filter(Product.title.contains(s)).all()
    prod_schema = ProductSchema(many=True)
    output = prod_schema.dump(query)
    return jsonify(output)

@app.route("/about")
def about():
    name = request.args.get('name')
    surname = request.args.get('surname')
    print(name)
    print(surname)
    return render_template('about.html', name=name, surname=surname)

@app.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        flash(f'Tu cuenta fue creada', 'success')
        return redirect(url_for('login'))
    return render_template('registration.html', title='Registration', form=form)

@app.route("/login", methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,
                form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Chequea el correo o la contraseña','danger')
    return render_template('login.html', title="Login", form=form)

@app.route("/account", methods=["GET","POST"])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Tu cuenta fue actualizada', 'success')
        return redirect(url_for('account'))
    return render_template('account.html', title='Cuenta', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

print(app.root_path)

# @app.route("/chart")
# def chart():
