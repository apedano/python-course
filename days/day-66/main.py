import random
from typing import List

from flask import Flask, jsonify, render_template, request, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, func
from wtforms import ValidationError

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
api_key = "soijfo09342rwe09fujsdnasi7u4wyn"


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dto_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            if column.name != 'id':
                # Create a new dictionary entry;
                # where the key is the name of the column
                # and the value is the value of the column
                dictionary[column.name] = getattr(self, column.name)
        return dictionary

def validate_name(name):
    existing_name = db.session.query(Cafe).filter_by(name=name).first()
    if existing_name:
        raise ValidationError(f"A cafe with name [{name}] already exists in the database.")


with app.app_context():
    db.create_all()

def create_error_json(error_message):
    return jsonify({'error': error_message})

def create_success_response(message):
    return jsonify({'response': {'success': True, 'message': message}}), 200

def create_json_response_from(cafes: List[Cafe]) -> Response:
    cafe_dtos = list(map(lambda cafe: cafe.to_dto_dict(), cafes))
    return jsonify(cafes=cafe_dtos)

@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

@app.route("/random")
def get_random_cafe():
    count = db.session.query(func.count(Cafe.id)).scalar()
    offset = random.randint(0, count - 1)
    random_cafe = db.session.query(Cafe).offset(offset).limit(1).first()
    return jsonify(random_cafe.to_dto_dict())

@app.route("/all")
def get_all_cafe():
    cafes = db.session.query(Cafe).all()
    return create_json_response_from(cafes)

@app.route("/search")
def get_search_by_location():
    location = request.args.get('location')
    if not location or location == '':
        return create_error_json("No location provided in the query parameters"), 400
    cafes = (db.session.query(Cafe)
                     .filter(func.lower(Cafe.location) == location.lower())
    .all())
    if len(cafes) == 0:
        return create_error_json(f"No cafes found for location [{location}]")
    else:
        return create_json_response_from(cafes)

# HTTP POST - Create Record

@app.route("/", methods=["POST"])
def add_cafe():
    try:
        validate_name(request.form.get("name"))
        cafe = Cafe(name=request.form.get("name"),
                    location=request.form.get("location"),
                    map_url= request.form.get("map_url"),
                    img_url= request.form.get("img_url"),
                    seats= request.form.get("seats"),
                    has_toilet= bool(request.form.get("has_toilet")),
                    has_wifi= bool(request.form.get("has_wifi")),
                    has_sockets= bool(request.form.get("has_sockets")),
                    can_take_calls= bool(request.form.get("can_take_calls")),
                    coffee_price= request.form.get("coffee_price")
        )


        db.session.add(cafe)
        db.session.commit()  # needed to persist the data
        return create_success_response("Successfully added cafe.")
    except Exception as err:
        return create_error_json(str(err)), 400


# HTTP PUT/PATCH - Update Record
@app.route("/update_price/<name>", methods=["PATCH"])
def update_price(name):
    try:

        new_price = request.args.get('new_price')
        if not new_price or new_price == '':
            return create_error_json("No [new_price] provided in the query parameters"), 400
        cafe = Cafe.query.filter_by(name=name).first()
        if not cafe:
            return create_error_json(f"Cafe with name [{name}] does not exist in the database."), 400
        cafe.coffee_price = new_price
        db.session.commit()
        return create_success_response("Successfully updated cafe price.")
    except Exception as err:
        return create_error_json(str(err)), 400

# HTTP DELETE - Delete Record
@app.route("/<name>", methods=["DELETE"])
def delete_cafe(name):
    try:
        if (request.headers.get("X-API-Key") is None
                or request.headers.get("X-API-Key") == ""):
            return create_error_json("No [X-API-Key] header present"), 403
        if request.headers.get("X-API-Key") != api_key:
            return create_error_json("[X-API-Key] header validation failed"), 403
        cafe = Cafe.query.filter_by(name=name).first()
        if not cafe:
            return create_error_json(f"Cafe with name [{name}] does not exist in the database."), 400
        db.session.delete(cafe)
        db.session.commit()  # needed to persist the data
        return create_success_response("Successfully delete cafe.")
    except Exception as err:
        return create_error_json(str(err)), 400


if __name__ == '__main__':
    app.run(debug=True)
