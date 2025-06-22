# Use Ubuntu as base
FROM ubuntu:22.04

# Prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Create non-root user
RUN useradd -ms /bin/bash user

# Install required packages
RUN apt update && apt install -y \
    netcat-traditional \
    bash \
    && rm -rf /var/lib/apt/lists/*

# Prevent hostname resolution error
RUN echo "127.0.0.1 $(hostname)" >> /etc/hosts

# Create editable folder for the user
RUN mkdir -p /home/editable && \
    chown user:user /home/editable && \
    echo "Welcome. Edit this file." > /home/editable/info.txt

# Set working directory
WORKDIR /home/editable

EXPOSE 9001

# Start a netcat listener on port 9001 and run bash as the unprivileged user
CMD ["bash", "-c", "nc.traditional -lkp 9001 -e su -s /bin/bash user"]
