# Use an official Python runtime as a parent image
FROM python:3.10.0

# Set the working directory to /app
WORKDIR /main

# Copy the current directory contents into the container at /app
COPY . /main

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt


# Define environment variable
ENV NAME World


# Expose port 8501 for the Streamlit app
EXPOSE 8501

# Run the Streamlit app when the container launches
CMD ["streamlit", "run", "main.py", "--server.port", "8503"]