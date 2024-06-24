# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app


# Install wget and any dependencies
RUN apt-get update && \
    apt-get install -y wget && \
    rm -rf /var/lib/apt/lists/*


# Copy the requirements.txt file into the container at /app
COPY requirements.txt requirements.txt

# Install any dependencies
RUN python -m pip install --upgrade pip && python -m pip install -r requirements.txt

# Copy the rest of the working directory contents into the container at /app
COPY . .

# Download the trained models
RUN   wget -O constants/weights/best_tomato_leaf_inceptionV3_256.h5 https://techwarriors-objectstorage-test.s3.us-south.cloud-object-storage.appdomain.cloud/best_tomato_leaf_inceptionV3_256.h5
RUN  wget -O constants/weights/best_rice_leaf.h5 https://techwarriors-objectstorage-test.s3.us-south.cloud-object-storage.appdomain.cloud/best_rice_leaf.h5

# Expose port 5001 for the Flask app
EXPOSE 5001
EXPOSE 8000

# Command to run the Flask app
CMD ["python", "main.py"]