#!/bin/bash
# Exit immediately if a command exits with a non-zero status
set -e

# Navigate to your project directory on EC2
cd /home/ubuntu/mlops-71052410026

# Stop and remove the old container if it exists
docker stop mlops-71052410026 || true
docker rm mlops-71052410026 || true

# Build the new Docker image
docker build -t mlops-71052410026 .

# Run the new container on port 80 mapping to 5000
docker run -d -p 80:5000 --restart always --name mlops-71052410026 mlops-71052410026
