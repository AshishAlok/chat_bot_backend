REM Step 1: Build the Docker image for the frontend
docker build -t backend .

REM Step 2: Run the Docker image in a container named frontend-container
docker run -d -p 8000:8000 --name backend-container backend
