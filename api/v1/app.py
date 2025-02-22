#!/usr/bin/python3
"""
This module defines the Flask application.
"""

from flask import Flask
from models import storage
from api.v1.views import app_views
from flask_cors import CORS
import os

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Calls storage.close() at the end of the request.
    """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """
    JSON 404 error response.
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', '5000'))
    app.run(host=host, port=port, threaded=True)
