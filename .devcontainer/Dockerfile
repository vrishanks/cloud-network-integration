FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

# Install necessary packages
RUN apt-get update && apt-get install -y \
  openvpn \
  iproute2 \
  iputils-ping \
  && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY src/app/requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

# Copy scripts
COPY scripts/ /usr/local/bin/
