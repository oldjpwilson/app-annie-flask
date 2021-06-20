from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from get_site_data import get_people

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    title = db.Column(db.String(120))

    def __repr__(self) -> str:
        return f"{self.name} -- {self.title}"


# for p in a:
#     print(p["name"], "\n")


@app.route("/people/json")
def howdy():
    a = get_people()
    return "Does this work??? '\n' {}".format(a)


@app.route("/mich")
def hi():
    return "Howdy Michelley"
