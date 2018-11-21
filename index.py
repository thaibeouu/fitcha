import os
import json
import datetime
from typing import List
from flask import Flask, render_template, request
from sqlalchemy import and_
from flask_sqlalchemy import SQLAlchemy


def create_app(test_config=None):
    project_dir = os.path.dirname(os.path.abspath(__file__))
    flask_app = Flask(__name__)
    if test_config is None:
        database_file = "sqlite:///{}".format(os.path.join(project_dir, "features.db"))
        flask_app.config["SQLALCHEMY_DATABASE_URI"] = database_file
        flask_app.templates_auto_reload = True
        flask_app.debug = True
    else:
        flask_app.config.update(test_config)
        flask_app.testing = True
        database_file = "sqlite:///{}".format(os.path.join(project_dir, "features_test.db"))
        flask_app.config["SQLALCHEMY_DATABASE_URI"] = database_file

    @flask_app.route("/", methods=["GET"])
    def index():
        return render_template("index.html")

    @flask_app.route("/features", methods=["GET"])
    def features_list():
        """Show all the requests, ordered by default."""
        features = Feature.query.all()
        list_dict = list(map(lambda x: x.as_dict(), features))
        return json.dumps(list_dict, default=json_serial)

    @flask_app.route("/features/add", methods=["POST"])
    def add():
        """Add new feature request with data taken from the AJAX request."""
        feature = None
        try:
            request_clone = request.json
            if "target_date" in request_clone:
                request_clone["target_date"] = datetime.datetime.strptime(request.json["target_date"], "%Y-%m-%d")
            feature = Feature(**request_clone)
            features_filtered = \
                Feature.query.filter(and_(Feature.client == request_clone["client"],
                                          Feature.client_priority >= int(request_clone["client_priority"]))).all()
            if features_filtered.__len__() > 0:
                priorities: List[int] = [f.client_priority for f in features_filtered]
                if int(request_clone["client_priority"]) in priorities:
                    for f in features_filtered:
                        f.client_priority += 1
            db.session.add(feature)
            db.session.commit()
        except Exception as e:
            print("Error: ", e)
        finally:
            if feature is not None:
                return json.dumps(feature.as_dict(), default=json_serial)
            return "Error adding new feature request"

    @flask_app.route("/features/delete", methods=["POST"])
    def delete():
        """Delete a feature request with given ID as args from the AJAX request."""
        feature = Feature.query.filter_by(id=request.args.get("id")).first()
        db.session.delete(feature)
        db.session.commit()
        return "Request successfully deleted"

    return flask_app


def init_db():
    flask_db = SQLAlchemy(app)
    flask_db.create_all()

    return flask_db


app = create_app()
db = init_db()


def json_serial(obj):
    """Handle datetime difference between Python and JavaScript."""
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


class Feature(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    client = db.Column(db.String(64), nullable=False)
    client_priority = db.Column(db.Integer, nullable=False)
    target_date = db.Column(db.Date)
    product_area = db.Column(db.String(64), nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


if __name__ == "__main__":
    app.run()
