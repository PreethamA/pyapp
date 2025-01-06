# Use a lightweight Python image as the base
FROM python:3.11-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

EXPOSE 5001

CMD ["python3", "appy.py"]