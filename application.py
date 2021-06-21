from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from get_site_data import get_people

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    title = db.Column(db.String(120))
    profile_image = db.Column(db.String(320))

    def __repr__(self) -> str:
        return f"{self.name} -- {self.title}"


people = get_people()  # move this outside the function
# Now, add the data from this, into the db

for p in people:
    exists = Person.query.filter_by(name=p["name"]).first()
    if not exists:
        person = Person(
            name=p["name"], title=p["title"], profile_image=p["profile_image"]
        )
        db.session.add(person)
        db.session.commit()
        # print(p["name"], " - ", p["profile_image"], "\n")
        print("adding")


@app.route("/")
def welcome():
    return "Welcome, please head to https://github.com/oldjpwilson/app-annie-flask or a url endpoint, eg: people/json, or person/3/json"


@app.route("/people/json")
def get_people():
    people = Person.query.all()
    all_people = []
    for p in people:
        print("{0} - {1}".format(p.name, p.id))
        all_people.append(
            {"name": p.name, "title": p.title, "profile_img": p.profile_image}
        )
    return {"people": all_people}


@app.route("/person/<id>/json")
def get_person(id):
    person = Person.query.get_or_404(
        id,
        "We are unable to locate the AppAnnie employee with that id. \nPlease try another id.",
    )
    print(person.name, "  you know")
    return jsonify(
        {
            "name": person.name,
            "title": person.title,
            "profile_img": person.profile_image,
        }
    )
