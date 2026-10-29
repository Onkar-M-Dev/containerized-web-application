FROM python:3.11-slim

# Prevent Python from buffering logs
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies (required for psycopg2)
RUN apt-get update && apt-get install -y gcc libpq-dev

# Copy dependencies first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 5000

# Run app
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:5000", "run:app"]