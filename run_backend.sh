#!/bin/bash

# Step 1: Log in to Hugging Face with the provided token
huggingface-cli login --token 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

# Step 2: Build the Docker image for the backend
docker build -t backend .

# Step 3: Run the Docker image in a container named backend-container
docker run -d -p 8000:8000 --name backend-container backend
