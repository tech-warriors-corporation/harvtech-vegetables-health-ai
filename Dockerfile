# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app


# Install wget and any dependencies
RUN apt-get update && apt-get install -y wget python3-opencv  && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file into the container at /app
COPY requirements.txt requirements.txt

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the working directory contents into the container at /app
COPY . .

# Make the setup.sh script executable
# RUN chmod +x setupModels.sh

# Run the setup script
# RUN ./setupModels.sh

RUN   wget -O constants/weights/best_tomato_leaf_inceptionV3_256.h5 https://techwarriors-objectstorage-test.s3.us-south.cloud-object-storage.appdomain.cloud/best_tomato_leaf_inceptionV3_256.h5

RUN  wget -O constants/weights/best_rice_leaf.h5 https://techwarriors-objectstorage-test.s3.us-south.cloud-object-storage.appdomain.cloud/best_rice_leaf.h5

# Expose port 5000 for the Flask app
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
