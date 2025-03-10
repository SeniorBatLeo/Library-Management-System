#!/bin/env python
"""
This script runs the Library_Management_System application using a development server.
"""

import os
#from models import db

from Library_Management_System import app as application
from Library_Management_System import db
from Library_Management_System.views import main

application.register_blueprint(main)
with application.app_context():
    db.create_all()
if __name__ == "__main__":
    HOST = os.environ.get("SERVER_HOST", "localhost")
    try:
        PORT = int(os.environ.get("SERVER_PORT", "80"))
    except ValueError:
        PORT = 80
    application.run(HOST, PORT, threaded=True)
