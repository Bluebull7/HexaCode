import os
import logging
from flask import Blueprint, send_from_directory, jsonify, request

# Create a Blueprint for the API routes
api_blueprint = Blueprint("api", __name__)

# Configure Logging
logging.basicConfig(
    level=logging.INFO,  # Log level
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
)
logger = logging.getLogger(__name__)

# Base directory for documentation files
DOCS_DIR = os.path.join(os.getcwd(), "static_docs/html")

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
