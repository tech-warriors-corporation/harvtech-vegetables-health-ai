#!/bin/bash

# Variables
COUNTRY="BR"
STATE="Sao Paulo"
LOCALITY="City"
ORGANIZATION="TechWarriors"
ORG_UNIT="Development"
COMMON_NAME="localhost"
DAYS=365
KEY_PATH="certs/key.pem"
CERT_PATH="certs/cert.pem"

# Create the /app directory if it does not exist
mkdir -p certs

# Generate the self-signed certificate
openssl req -x509 -nodes -days $DAYS -newkey rsa:2048 \
    -keyout $KEY_PATH \
    -out $CERT_PATH \
    -subj "/C=$COUNTRY/ST=$STATE/L=$LOCALITY/O=$ORGANIZATION/OU=$ORG_UNIT/CN=$COMMON_NAME"

# Display success message
echo "Self-signed certificate and key have been generatedin $PWD"
