"""contains configuration options for the server
"""
import os
from sqlalchemy.engine import Engine
from sqlalchemy import event

# Statement for enabling the development environment
DEBUG = True
LOGIN_DISABLED = True
PRESERVE_CONTEXT_ON_EXCEPTION = False

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
SQLALCHEMY_DATABASE_URI = 'sqlite:///'
DATABASE_CONNECT_OPTIONS = {}

# Enable protection agains (CSRF)
CSRF_ENABLED = False

#Secret key for CSRF
WTF_CSRF_SECRET_KEY = "secret"
WTF_CSRF_METHODS = []

# Secret key for signing cookies
SECRET_KEY = "secret"

# Set the port and server name
SERVER_NAME = "localhost:8080"

SQLALCHEMY_TRACK_MODIFICATIONS = False
 
#set foreign_keys on for sqlite. these are off by default
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, _connection_record):
    """sets sqlite3 'PRAGMA foreign_keys=ON'
    """
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
