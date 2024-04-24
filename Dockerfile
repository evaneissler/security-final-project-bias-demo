# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /root

# Copy the current directory contents into the container at /app
COPY ./config /root

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y \
    bash \
    vim \
 && rm -rf /var/lib/apt/lists/*

# Install pandas
RUN pip install --no-cache-dir pandas

# Install scikit-learn
RUN pip install --no-cache-dir scikit-learn

# Install numpy
RUN pip install --no-cache-dir numpy

# Define environment variable
ENV PYTHONUNBUFFERED=TRUE

