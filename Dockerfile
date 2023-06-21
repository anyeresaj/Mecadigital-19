# Start from a base image with Python 3.11
FROM python:3.11-slim-buster

# Set the working directory in the Docker container
WORKDIR /app

# Copy the requirements.txt to the Docker container
COPY requirements.txt requirements.txt

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of the code to the Docker container
COPY . .

# Set the command to run when the Docker container starts
CMD exec gunicorn --bind :${PORT:-5000} app:app
