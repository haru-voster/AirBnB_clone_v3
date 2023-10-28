#!/usr/bin/python3
"""Starts a Flask web aplication.

The aplication listens on 0.0.0.0, port 5000.
Routes:
    /states_list: HTML page with a list of all State objects in DBStorage.
"""
from models import storage
from flask import Flask
from flask import render_template

ap = Flask(__name__)


@ap.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all State objects in DBStorage.

    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@ap.teardown_apcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    ap.run(host="0.0.0.0")