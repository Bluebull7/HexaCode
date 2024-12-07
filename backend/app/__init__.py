from flask import Flask
from flask_cors import CORS

def create_app():
    """
    Factory function to create and configure the Flask app.
    """
    app = Flask(__name__)
    
    # Enable CORS for all routes
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Register Blueprints
    from app.routes import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api")
    
    return app
