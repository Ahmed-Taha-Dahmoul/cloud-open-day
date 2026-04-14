# Use official Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the project code
COPY . .

# Expose the port Django runs on
EXPOSE 8000

# Run the Django development server (simple for demo purposes)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]