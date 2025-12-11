# Set the python version as a build-time argument
ARG PYTHON_VERSION=3.12-slim-bullseye
FROM python:${PYTHON_VERSION}

# Create virtualenv
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Python settings
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# OS dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    libjpeg-dev \
    libcairo2 \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Working directory
WORKDIR /code

# Copy project files
COPY requirements.txt /tmp/requirements.txt
COPY ./src /code

# Install Python deps
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt

# Copy and make startup script executable
COPY ./boot/docker-run.sh /opt/docker-run.sh
RUN chmod +x /opt/docker-run.sh

# Final command
CMD ["/opt/docker-run.sh"]