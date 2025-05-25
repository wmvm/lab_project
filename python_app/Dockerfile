# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy app files
COPY python_app/lab_app.py .

# Install Flask
RUN pip install flask

# Expose the Flask port
EXPOSE 5000

# Run the application
CMD ["python", "lab_app.py"]
