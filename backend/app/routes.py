from flask import Blueprint, request, jsonify, send_from_directory
from werkzeug.exceptions import HTTPException
import logging
import os
from app.interpreter import tokenize, execute

# Initialize the logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Create a blueprint for the API
api_blueprint = Blueprint("api", __name__)

# Serve the HexaCode Playground API
@api_blueprint.route('/execute', methods=['POST'])
def execute_code():
    """
    Endpoint to execute HexaCode scripts.
    """
    try:
        # Parse incoming data
        data = request.json
        if not data or "script" not in data:
            logger.warning("No script provided in the request body.")
            return jsonify({"error": "No script provided"}), 400
        
        script = data.get("script", "").strip()
        if not script:
            logger.warning("Empty script provided.")
            return jsonify({"error": "Empty script provided"}), 400

        # Process the script
        logger.info("Executing script: %s", script)
        tokens = tokenize(script)  # Assuming tokenize is defined
        output = []
        execute(tokens, print_callback=lambda x: output.append(x))  # Assuming execute is defined

        # Return successful response
        logger.info("Execution completed successfully.")
        return jsonify({"output": "\n".join(output)})
    
    except Exception as e:
        # Log and handle unexpected errors
        logger.error("An unexpected error occurred: %s", str(e), exc_info=True)
        return jsonify({"error": "Internal server error"}), 500

# Serve documentation files
api_blueprint.route('/docs/<path:filename>', methods=['GET'])
def serve_docs(filename):
    """
    Endpoint to serve Sphinx documentation files.
    """
    docs_dir = os.path.join(os.getcwd(), "static_docs")
    try:
        return send_from_directory(docs_dir, filename)
    except FileNotFoundError:
        return jsonify({"error": "Documentation file not found"}), 404

# Redirect /docs/ to the documentation index
@api_blueprint.route('/docs/', methods=['GET'])
def serve_docs_index():
    """
    Endpoint to serve the documentation index page.
    """
    docs_dir = os.path.join(os.getcwd(), "static_docs")
    return send_from_directory(docs_dir, "index.html")
# Handle HTTP errors globally
@api_blueprint.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Handles HTTP exceptions gracefully.
    """
    logger.warning("HTTP error occurred: %s", e.description)
    return jsonify({"error": e.description}), e.code

# Handle other uncaught exceptions globally
@api_blueprint.errorhandler(Exception)
def handle_exception(e):
    """
    Handles uncaught exceptions gracefully.
    """
    logger.error("Uncaught exception: %s", str(e), exc_info=True)
    return jsonify({"error": "An unexpected error occurred"}), 500
