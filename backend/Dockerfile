# Use a lightweight Python image
FROM python:3.10-slim

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
