# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app


# Install wget and any dependencies
RUN apt-get update && \
    apt-get install -y wget openssl libglib2.0-0 \
    python3-opencv libgl1-mesa-dev && \
    rm -rf /var/lib/apt/lists/*


# Copy the requirements.txt file into the container at /app
COPY requirements.txt requirements.txt

# Install any dependencies
RUN python -m pip install --upgrade pip && python -m pip install -r requirements.txt


# Copy the scripts to the Docker image (assuming they are in the same directory as the Dockerfile)
COPY generate_certificates.sh /generate_certificates.sh
COPY download_models.sh /download_models.sh

# Make the scripts executable
RUN chmod +x /generate_certificates.sh && \
chmod +x /download_models.sh

# Copy the rest of the working directory contents into the container at /app
COPY . .

# Run the script to generate certificates
RUN /generate_certificates.sh

# Download the trained models
RUN  /download_models.sh

# Expose port 5001 for the Flask app
EXPOSE 5001
EXPOSE 8000

# Command to run the Flask app
CMD ["python3", "main.py"]