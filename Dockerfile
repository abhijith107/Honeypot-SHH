

FROM python:3.9-slim


COPY ssh_honeypot.py /


EXPOSE 2222


CMD ["python", "/ssh_honeypot.py"]



FROM python:3.9-slim

# Copy HTTP honeypot script
COPY http_honeypot.py /

# Expose HTTP port
EXPOSE 8080

# Run HTTP honeypot script
CMD ["python", "/http_honeypot.py"]

