# CONCEPT: Containerization
# Creating a secure space that contains everything the app needs to run.

# Pulls the official Python interpreter image to run the application
FROM python:3.9-slim

# Sets the working directory inside the container
WORKDIR /app

# Copies the application into the workspace
COPY payroll_security.py .

# Creates a non-root user to prevent unauthorized privilege escalation
RUN useradd -m appuser
USER appuser

# Run the app automatically when the container starts
CMD ["python", "payroll_security.py"]