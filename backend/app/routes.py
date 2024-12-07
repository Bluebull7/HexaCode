import os
import logging
from flask import Blueprint, send_from_directory, jsonify, request
from app.interpreter import tokenize, execute
from werkzeug.exceptions import HTTPException
# Create a Blueprint for the API routes
api_blueprint = Blueprint("api", __name__)

# Configure Logging
logging.basicConfig(
    level=logging.INFO,  # Log level
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
)
logger = logging.getLogger(__name__)

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


# Base directory for documentation files
DOCS_DIR = os.path.join(os.getcwd(), "app/static_docs/html")

@api_blueprint.route('/docs/<path:filename>', methods=['GET'])
def serve_docs(filename):
    """
    Serve specific documentation files, including _static and _sources.
    """
    try:
        full_path = os.path.join(DOCS_DIR, filename)
        logger.info(f"Request for file: {filename} (resolved path: {full_path})")

        # Check if the file exists before serving
        if not os.path.exists(full_path):
            logger.error(f"File not found: {full_path}")
            return jsonify({"error": f"File {filename} not found"}), 404

        # Serve the file
        return send_from_directory(DOCS_DIR, filename)
    except Exception as e:
        logger.exception(f"Unexpected error while serving file: {filename}")
        return jsonify({"error": "An unexpected error occurred"}), 500


@api_blueprint.route('/docs/', methods=['GET'])
def serve_docs_index():
    """
    Serve the index.html file for /docs/.
    """
    try:
        index_path = os.path.join(DOCS_DIR, "index.html")
        logger.info(f"Request for docs index (resolved path: {index_path})")

        # Check if the index.html file exists
        if not os.path.exists(index_path):
            logger.error(f"index.html file not found at: {index_path}")
            return jsonify({"error": "index.html file not found"}), 404

        # Serve the index.html file
        return send_from_directory(DOCS_DIR, "index.html")
    except Exception as e:
        logger.exception("Unexpected error while serving docs index")
        return jsonify({"error": "An unexpected error occurred"}), 500
