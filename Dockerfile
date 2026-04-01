# CONCEPT: Containerization
# We are creating a 'Secure Bubble' that has everything the app needs to run.

# Use the official lightweight Python image
FROM python:3.9-slim

# Set the 'Workplace' inside the container
WORKDIR /app

# Copy the script into the bubble
COPY payroll_security.py .

# Run the app automatically when the container starts
CMD ["python", "payroll_security.py"]