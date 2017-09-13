"""Run a test server.
"""
from flaskserver.app import create_app
app = create_app("test_config")
app.run(host="0.0.0.0", port=8080, threaded=True)
