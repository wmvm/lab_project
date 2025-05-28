# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy app files
COPY python_app/* .

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Run the application
# CMD ["python", "lab_app.py"]
CMD ["gunicorn", "lab_app:app", "--bind", "0.0.0.0:5000"]
