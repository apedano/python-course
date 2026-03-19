# 🐍 Create RESTful services with Flask

## Example
| Endpoint            | Method | Description                  | Success Response | Error Codes                          |
|--------------------|--------|------------------------------|------------------|--------------------------------------|
| /api/items         | GET    | Get all items                | 200 OK           | 500 Internal Server Error            |
| /api/items/{id}    | GET    | Get item by ID               | 200 OK           | 404 Not Found, 400 Bad Request       |
| /api/items         | POST   | Create a new item            | 201 Created      | 400 Bad Request, 409 Conflict        |
| /api/items/{id}    | PUT    | Update entire item           | 200 OK           | 400 Bad Request, 404 Not Found       |
| /api/items/{id}    | PATCH  | Partially update item        | 200 OK           | 400 Bad Request, 404 Not Found       |
| /api/items/{id}    | DELETE | Delete item                  | 204 No Content   | 404 Not Found                        |
| /api/auth/login    | POST   | Authenticate user            | 200 OK           | 401 Unauthorized, 400 Bad Request    |
| /api/auth/register | POST   | Register new user            | 201 Created      | 400 Bad Request, 409 Conflict        |

| Code | Meaning                  | When to Use                                      |
|------|--------------------------|--------------------------------------------------|
| 400  | Bad Request              | Invalid input / validation errors                |
| 401  | Unauthorized             | Missing or invalid authentication                |
| 403  | Forbidden                | Authenticated but not allowed                    |
| 404  | Not Found                | Resource does not exist                          |
| 409  | Conflict                 | Duplicate resource / state conflict              |
| 422  | Unprocessable Entity     | Semantic validation errors                       |
| 500  | Internal Server Error    | Unexpected server failure                        |
| 503  | Service Unavailable      | Server temporarily unavailable                   |

```python
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
```

## `GET` requests
Get single record
```python
# HTTP GET - Read Record

@app.route("/random")
def get_random_cafe():
    count = db.session.query(func.count(Cafe.id)).scalar()
    offset = random.randint(0, count - 1)
    random_cafe = db.session.query(Cafe).offset(offset).limit(1).first()
    return jsonify(random_cafe.to_dto_dict())
```

Get all records
```python
@app.route("/all")
def get_all_cafe():
    cafes = db.session.query(Cafe).all()
    return create_json_response_from(cafes)
```

Get record by request query parameters `location`
```python
@app.route("/search")
def get_search_by_location():
    location = request.args.get('location')
    if not location or location == '':
        return create_error_json("No location provided in the query parameters"), 400
    cafes = (db.session.query(Cafe)
                     .filter(func.lower(Cafe.location) == location.lower())
    .all())
    if len(cafes) == 0:
        return create_error_json(f"No cafes found for location [{location}]"), 400
    else:
        return create_json_response_from(cafes)
```

## `POST` requests


### Create a request as a filled form
Add a new record with the header `'Content-Type': 'application/x-www-form-urlencoded'`

and the body:

```
name=Cafe%20della%20cattedrale&location=Palermo&map_url=https%3A%2F%2Fwww.google.com%2Fmaps%2Fsearch%2F%3Fapi%3D1%26query%3DPalermo%2520Cathedral%2520Via%2520Vittorio%2520Emanuele%2C%2520490%2C%252090134-%2520Under%2520Review%2520-%26query_place_id%3DChIJySXqmGHvGRMRancw-ZBf2ow&img_url=https%3A%2F%2Flaptopfriendly.co%2Fimages%2Fplaces%2Funder-review%2Fpalermo-cathedral%2Fpalermo-cathedral--under-review.jpg&seats=30&has_toilet=True&has_wifi=True&can_take_calls=False&coffee_price=2.10&has_sockets=True
```

This make the request to be interpreted by Flask as a form accessible vis `request.form.get('<field_name>')`

Some of the parameters need conversion like ``has_wifi= bool(request.form.get("has_wifi"))``

```python
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
```

## `PATCH` requests

This differs from `PUT` requstes where we pass an entire item to replace the existing one on the same identifier

```python
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
```

## `DELETE` requests

The request check the validity of the `X-API-Key` to authorize the request

> Flask normalizes request header names so that lower case names without dashes will not be recognized

```python
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
```
