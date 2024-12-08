from flask import Blueprint, request, jsonify, send_from_directory
from werkzeug.exceptions import HTTPException
import logging
import os
from app.interpreter import HexaInterpreter

# Initialize the logger
logger = logging.getLogger(__name__)

# Create a blueprint for the API
api_blueprint = Blueprint("api", __name__)

# Initialize the HexaInterpreter
interpreter = HexaInterpreter()

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
        output = []
        interpreter.execute(script, print_callback=lambda x: output.append(x))

        # Return successful response
        logger.info("Execution completed successfully.")
        return jsonify({"output": "\n".join(output)})
    
    except SyntaxError as e:
        logger.warning("Syntax error during script execution: %s", str(e))
        return jsonify({"error": "Syntax Error", "message": str(e)}), 400

    except Exception as e:
        logger.error("Unexpected error during script execution: %s", str(e), exc_info=True)
        return jsonify({"error": "Internal server error"}), 500

# Serve React App (Frontend)
@api_blueprint.route("/", defaults={"path": ""})
@api_blueprint.route("/<path:path>")
def serve_react_app(path):
    """
    Serve React app for all routes except API.
    """
    try:
        react_build_dir = os.path.join(BASE_DIR, "react_build")
        file_path = os.path.join(react_build_dir, path)

        if os.path.exists(file_path):
            return send_from_directory(react_build_dir, path)
        else:
            # Serve React's index.html for unmatched frontend routes
            return send_from_directory(react_build_dir, "index.html")
    except FileNotFoundError:
        logger.error("React build directory or index.html not found.")
        return jsonify({"error": "React app not found"}), 404


@api_blueprint.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Handles HTTP exceptions gracefully.
    """
    logger.warning("HTTP error occurred: %s", e.description)
    return jsonify({"error": e.description}), e.code

@api_blueprint.errorhandler(Exception)
def handle_exception(e):
    """
    Handles uncaught exceptions gracefully.
    """
    logger.error("Uncaught exception: %s", str(e), exc_info=True)
    return jsonify({"error": "An unexpected error occurred"}), 500
