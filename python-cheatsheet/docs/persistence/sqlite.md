# 🐍 Persistence with SQLite and SQLAlchemy

## Import

```python
import sqlite3

db = sqlite3.connect("books-collection.db")
```

This refers to a local file `books-collection.db`

## The cursor

So a cursor is also known as the mouse or pointer. 
If we were working in Excel or Google Sheet, we would be using the cursor to add rows of data or edit/delete data, 
we also need a cursor to modify our SQLite database.

```python
cursor = db.cursor()

cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
```

```python
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()
```

### Tool to explore SQLite dbs

https://sqlitebrowser.org/dl/

## SQLAlchemy
SQLAlchemy is defined as an **ORM** (_Object Relational Mapping_) library. 
This means that it's able to map the relationships in the database into Objects. 
Fields become Object properties. 
Tables can be defined as separate Classes and each row of data is a new Object. 
This will make more sense after we write some code and see how we can create a Database/Table/Row of data using SQLAlchemy.

### Installation

``
pip install flask_sqlalchemy
pip install SQLAlchemy
``

### Application initialization

```python
app = Flask(__name__)

# Defines the project's ORM base class
#In this case we don't add anything on top of the base DeclarativeBase class
class Base(DeclarativeBase):
    pass

#This will make the db point to a sqlite db on the new-books-collection.db file
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

# Create the SQLAlchemy extension with the Base class as base class for all model classes
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)



```

### The `DeclarativeBase` class

https://flask-sqlalchemy.palletsprojects.com/en/stable/quickstart/#initialize-the-extension

`DeclarativeBase` is a class from SQLAlchemy that provides the foundation for ORM models.

It contains the internal machinery that:

* maps Python classes to database tables

* maps class attributes to table columns

* manages metadata about tables

So when we create model classes

```python
class Book(Base):
    pass

class Author(Base):
    pass
```

This lets SQLAlchemy keep track of all models in one metadata registry.

Internally SQLAlchemy stores something like:

```
Base.metadata
   ├── Book table
   └── Author table
```

This is what allows:

```python
    db.create_all()
```

to automatically create every table defined in your models.

Because all models share `Base`, SQLAlchemy can:

* register tables automatically
 
* generate schema

* manage relationships

* build queries

Example:

```python
Base.metadata.tables
```

might contain:

```json
{
    "book": Table(...)
}
```

### Create the schema classes

```python
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'
```

### Initialise all schema classes into the db

https://flask-sqlalchemy.palletsprojects.com/en/stable/models/#defining-models

Subclass `db.Model` to create a model class. 
Unlike plain SQLAlchemy, Flask-SQLAlchemy’s model will automatically generate a table name if `__tablename__` is not set 
and a primary key column is defined.


Defining a model does not create it in the database. 
Use `create_all()` to create the models and tables after defining them. 
If you define models in submodules, you must import them so that SQLAlchemy knows about them before calling create_all.

```python
# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()
```

Flask-SQLAlchemy checks the database and:

* Looks at all models registered in `Base.metadata`

* Checks if their tables exist in the database

* Creates only the missing tables

> no existing table is deleted neither modified 
> (if the model class has, for instance, a column changed or added)
> To apply model changes use **Flask-Migrate**

We can also initialize data in the db, checking if the row is present already

```python
# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()
    if not db.session.query(Book).filter_by(title="Harry Potter").first():
        new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
        db.session.add(new_book)
        db.session.commit()
```

### Session basics

Everything revolves around the session:

`add()` → stage insert

`commit()` → save to DB

`rollback()` → undo on error

```python
try:
    db.session.add(new_book)
    db.session.commit()
except:
    db.session.rollback()
```

### CRUD operations with SQLAlchemy

#### Insertion

```python
# Don’t set id manually (auto-generated)
new_book = Book(
    title="Harry Potter",
    author="J. K. Rowling",
    rating=9.3
)

db.session.add(new_book)
db.session.commit() #needed to persist the data
```

#### Read

Get all records
```python
books = db.session.query(Book).all()
```

Get by primary key
```python
book = db.session.get(Book, 1)
```

Filter
```python
book = db.session.query(Book).filter_by(title="Harry Potter").first()
```

More complex filters (SQL expression language)

```python
from sqlalchemy import select

stm = select(Book).where(Book.rating > 8) 
books = db.session.execute(stm).scalars().all()
```

Basic SQL can also be used, but the result is a `row` object

```python
from sqlalchemy import text

result = db.session.execute(
    text("SELECT * FROM book WHERE rating > :rating"),
    {"rating": 8}
)

books = result.fetchall()
#row is not a Book object, but a row result
for row in books:
    print(row.title, row.author)
```

To get ORM objects from raw results

```python
result = db.session.execute(
    text("SELECT * FROM book")
)

books = result.mappings().all()

for row in books:
    print(row["title"])
#OR
books = [Book(**row) for row in result.mappings()]
```

👉 Common helpers:

`.all()` → list

`.first()` → first result or None

`.scalars()` → unwrap ORM objects

#### UPDATE (Modify existing records)

Load and modify (most common)
```python
book = db.session.get(Book, 1)
book.rating = 9.5

db.session.commit()
```

Update via query
```python
db.session.query(Book).filter_by(id=1).update({
    Book.rating: 9.5
})
db.session.commit()
```

👉 First approach is preferred in most Flask apps.

#### DELETE (Remove records)
Delete a single record
```python
book = db.session.get(Book, 1)
db.session.delete(book)
db.session.commit()
```

Delete with filter
```python
db.session.query(Book).filter_by(title="Harry Potter").delete()
db.session.commit()
```
