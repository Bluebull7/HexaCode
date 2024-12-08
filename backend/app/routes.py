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

@api_blueprint.route('/docs/<path:filename>')
def serve_docs(filename):
    """
    Serve documentation files from static_docs.
    """
    try:
        # Path to static_docs
        docs_dir = os.path.join(os.path.dirname(__file__), "static_docs/html")
        
        # Log the request
        logger.info(f"Serving documentation file: {filename}")
        print(f"Resolved stati  c_docs path: {docs_dir}")

        # Serve the file
        return send_from_directory(docs_dir, filename)
    except FileNotFoundError:
        logger.warning(f"Documentation file not found: {filename}")
        return jsonify({"error": "Documentation file not found"}), 404
    except Exception as e:
        logger.error(f"Error serving documentation file: {e}", exc_info=True)
        return jsonify({"error": "Internal server error"}), 500

@api_blueprint.route('/docs/')
def serve_docs_index():
    """
    Serve the index page of the documentation.
    """
    try:
        # Path to static_docs
        docs_dir = os.path.join(os.path.dirname(__file__), "static_docs/html")
        
        # Log the request
        logger.info("Serving documentation index page.")
        
        # Serve index.html
        return send_from_directory(docs_dir, "index.html")
    except FileNotFoundError:
        logger.warning("Documentation index page not found.")
        return jsonify({"error": "Documentation index page not found"}), 404
    except Exception as e:
        logger.error(f"Error serving documentation index: {e}", exc_info=True)
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
