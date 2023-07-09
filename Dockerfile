# Base image
FROM python:3.9-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

RUN pip install --upgrade pip

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the code to the working directory
COPY . .

# Run the Python script
CMD ["python3", "-m", "Adarsh"]
