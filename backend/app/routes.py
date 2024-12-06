from flask import Blueprint, request, jsonify
from app.interpreter import tokenize, execute

# Create a blueprint for API routes
api_blueprint = Blueprint("api", __name__)

@api_blueprint.route('/execute', methods=['POST'])
def execute_code():
    """
    API endpoint to execute HexaCode scripts.
    """
    try:
        # Parse the incoming script from the request
        data = request.get_json()
        script = data.get("script", "").strip()

        # Validate input
        if not script:
            return jsonify({"error": "Empty script provided"}), 400

        # Tokenize and execute the script
        tokens = tokenize(script)
        output = []
        execute(tokens, print_callback=lambda x: output.append(x))

        # Return the result
        return jsonify({"output": "\n".join(output)})

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500
