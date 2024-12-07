from flask import Flask
from app.routes import api_blueprint  # Import your blueprint

app = Flask(__name__)

from flask_cors import CORS

CORS(app)

# Register the blueprint
app.register_blueprint(api_blueprint, url_prefix="/api")

# Optionally, define a root route
@app.route("/", methods=["GET"])
def home():
    return "Welcome to the HexaCode API!"


if __name__ == "__main__":
    app.run(debug=True)
