# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents (including the static folder) into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Streamlit uses (default is 8501)
EXPOSE 8000

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8000", "--server.enableCORS=false"]
