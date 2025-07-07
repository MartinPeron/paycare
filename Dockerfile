# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the Python dependencies
RUN pip install -r requirements.txt

# Test the application
CMD ["pytest", "."]

# Run the application
CMD ["python", "etl.py"]
