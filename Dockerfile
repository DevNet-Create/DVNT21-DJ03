FROM python:3-slim-buster

# Create the /app directory an set it as the default workspace
WORKDIR /app

# Copy the requirements.txt file inside the container
COPY requirements.txt .

# Install python requirements to ensure DJANGO is installed
RUN pip install -r requirements.txt --no-cache-dir

# Copy the contents of our DJANGO project into /app directory inside the container
COPY ./netprog .

# Upon container start, lets run DJANGO manage.py on port 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
