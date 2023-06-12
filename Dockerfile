# Use the official Python 3.11 image as the base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python code to the container
COPY . .

# Set the environment variables
ENV MONGODB_URI=mongodb://localhost:27017
ENV DATABASE_NAME=admin

# Run the Python script when the container starts
CMD ["python", "main.py", "ping", "500"]
