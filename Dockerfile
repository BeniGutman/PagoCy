# Use the official Python image from the Docker Hub
# FROM python:3.12-slim
FROM python

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

# Copy the current directory contents into the container at /app
COPY ./app /app/

# Expose the port the app runs on (this should match the port your app runs on)
EXPOSE 8000

# Command to run the FastAPI server using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
