# Use a tiny version of Python
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install Flask
RUN pip install flask

# Copy your app.py into the container
COPY app.py .

# Run the app
CMD ["python", "app.py"]