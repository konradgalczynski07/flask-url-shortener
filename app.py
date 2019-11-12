from flask import Flask, jsonify
from flask_restful import Api
from marshmallow import ValidationError

from db import db
from ma import ma
from resources.urls import RedirectUrlResource, ShortenUrlResource


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.secret_key = "very_secret"
api = Api(app)

api.add_resource(RedirectUrlResource, "/<string:shortened_url>")
api.add_resource(ShortenUrlResource, "/")


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


db.init_app(app)
@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    ma.init_app(app)
    app.run(port=5000)
