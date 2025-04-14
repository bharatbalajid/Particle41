# Visitor Info App

This is a simple Flask app that returns the current timestamp and the visitor's IP address in JSON format.

# Dockerfile Highlights

1. Multi-stage build for smaller images
2. Non-root user for security
3. Alpine base image for performance

# How to Run with Docker

```bash
docker build -t visitor-app .
docker run -p 5000:5000 visitor-app 