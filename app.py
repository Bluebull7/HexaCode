from app import create_app

# Create the Flask app using the factory
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
