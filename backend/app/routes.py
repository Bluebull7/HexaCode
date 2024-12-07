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
        tokens = interpreter.tokenize(script)
        output = []
        interpreter.execute(script, print_callback=lambda x: output.append(x))

        # Return successful response
        logger.info("Execution completed successfully.")
        return jsonify({"output": "\n".join(output)})
    
    except SyntaxError as e:
        # Handle script syntax errors
        logger.warning("Syntax error during script execution: %s", str(e))
        return jsonify({"error": "Syntax Error", "message": str(e)}), 400

    except Exception as e:
        # Log and handle unexpected errors
        logger.error("An unexpected error occurred: %s", str(e), exc_info=True)
        return jsonify({"error": "Internal server error"}), 500

@api_blueprint.route('/docs/<path:filename>')
def serve_docs(filename):
    """
    Endpoint to serve documentation files.
    """
    try:
        docs_dir = os.path.join(os.getcwd(), "static_docs")
        logger.info("Serving documentation file: %s", filename)
        return send_from_directory(docs_dir, filename)
    except FileNotFoundError:
        logger.warning("Documentation file not found: %s", filename)
        return jsonify({"error": "Documentation file not found"}), 404
    except Exception as e:
        logger.error("Error while serving documentation: %s", str(e), exc_info=True)
        return jsonify({"error": "Internal server error"}), 500

@api_blueprint.route('/docs/')
def serve_docs_index():
    """
    Endpoint to serve the index page of the documentation.
    """
    try:
        docs_dir = os.path.join(os.getcwd(), "static_docs")
        logger.info("Serving documentation index page.")
        return send_from_directory(docs_dir, "index.html")
    except FileNotFoundError:
        logger.warning("Documentation index page not found.")
        return jsonify({"error": "Documentation index page not found"}), 404
    except Exception as e:
        logger.error("Error while serving documentation index: %s", str(e), exc_info=True)
        return jsonify({"error": "Internal server error"}), 500

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
