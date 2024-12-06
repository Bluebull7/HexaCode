from flask import Blueprint, request, jsonify
from app.interpreter import tokenize, execute

# Create a blueprint for API routes
api_blueprint = Blueprint("api", __name__)

@api_blueprint.route('/execute', methods=['POST'])
def execute_code():
    """
    API endpoint to execute HexaCode scripts.
    """
    data = request.json
    script = data.get("script", "")
    tokens = tokenize(script)
    output = []

    def capture_output(content):
        output.append(content)

    execute(tokens, print_callback=capture_output)
    return jsonify({"output": "\n".join(output)})
