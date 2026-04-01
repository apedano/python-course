from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

#Configure Flask-login manager
login_manager = LoginManager()
login_manager.init_app(app)



# CREATE DATABASE

class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB


class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(100), unique=True, nullable=False)
  password = db.Column(db.String(100), nullable=False)
  name = db.Column(db.String(1000))


with app.app_context():
    db.create_all()


#load user callback function
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        user = User()
        user.email = request.form['email']
        user.name = request.form['name']
        user.password = generate_password_hash(password=request.form['password'], method='pbkdf2:sha256', salt_length=8)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return render_template("secrets.html", name=request.form.get('name'))


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('secrets', name=user.name))
        else:
            flash("Invalid email or password. Please try again.")
            return redirect(url_for('login'))
    return render_template("login.html")


@app.route('/secrets/<name>')
@login_required
def secrets(name):
    return render_template("secrets.html", name=name)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
def download():
    pass


if __name__ == "__main__":
    app.run(debug=True)
