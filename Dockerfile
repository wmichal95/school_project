# Base image
FROM python:3.9 as app_builder

# Working directory
WORKDIR /app

# Copy requirements.txt into /app
COPY requirements.txt requirements.txt

# install packages
RUN pip3 install -r requirements.txt

# copy all files to /app
COPY . .

# start application from makefile
CMD make run_server