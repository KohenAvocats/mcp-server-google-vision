FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY pyproject.toml README.md LICENSE ./
COPY src/ ./src/
COPY main.py ./

RUN pip install --no-cache-dir . uvicorn starlette

# Set environment variable placeholder
ENV GOOGLE_API_KEY=""
ENV PORT=8080

# Expose port
EXPOSE 8080

# Run the HTTP server
CMD ["python", "main.py"]
