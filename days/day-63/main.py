from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

app.config['SECRET_KEY'] = 'sdasdqwevcddcvsd'


##CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)


##CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()
    if not db.session.query(Book).filter_by(title="Harry Potter").first():
        new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
        db.session.add(new_book)
        db.session.commit()

# # CREATE RECORD
# with app.app_context():
#     new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
#     db.session.add(new_book)
#     db.session.commit()

class BookForm(FlaskForm):
    title = StringField('Book title', validators=[DataRequired(), Length(1, 64)])
    author = StringField("The author", validators=[DataRequired(), Length(1, 64)])
    rating = SelectField(
        "Rate the book",
        choices=[(str(i), str(i)) for i in range(1, 10)],
        coerce=int
    )
    submit = SubmitField('Submit')

    def validate_title(self, field):
        existing_book = db.session.query(Book).filter_by(title=field.data).first()
        if existing_book:
            raise ValidationError("This book already exists in the database.")

class ChangeBookRating(FlaskForm):
    rating = SelectField(
        "Rate the book",
        choices=[(str(i), str(i)) for i in range(1, 10)],
        coerce=int
    )
    submit = SubmitField('Submit')

@app.route('/')
def home():
    return render_template("index.html", books=Book.query.all())


@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()
    if form.validate_on_submit():
        try:
            new_book = Book(
                title=form.title.data,
                author=form.author.data,
                rating=form.rating.data
            )
            db.session.add(new_book)
            db.session.commit()  # needed to persist the data
            return redirect(url_for("home"))
        except:
            db.session.rollback()
            return redirect(url_for("home"))
    return render_template("add.html", form=form)

@app.route("/delete/<int:book_id>", methods=["GET", "POST"])
def delete_page(book_id):
    if request.method == "GET":
        book = db.session.query(Book).filter_by(id=book_id).first()
        return render_template("delete.html", book=book)
    else:
        book = db.session.get(Book, book_id)
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for("home"))

@app.route("/change_rating/<int:book_id>", methods=["GET", "POST"])
def change_rating_page(book_id):
    book = db.session.get(Book, book_id)
    form = ChangeBookRating(obj=book)
    if request.method == "GET":
        return render_template("change_rating.html", form=form, book=book)
    else:
        db.session.query(Book).filter_by(id=book_id).update({
            Book.rating: form.rating.data
        })
        db.session.commit()
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

