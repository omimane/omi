# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies (make sure you have a requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable to disable the Streamlit welcome message
ENV STREAMLIT_DISABLE_WELCOME_MESSAGE=true

# Expose port for Streamlit
EXPOSE 8501

# Command to run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.headless", "true", "--server.port", "8501"]
