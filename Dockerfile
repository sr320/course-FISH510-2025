FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Copy repository
COPY . /app

# Install dependencies from chatbot subdir
RUN pip install --upgrade pip \
 && pip install -r chatbot/requirements.txt

# Expose port (Railway sets PORT env var)
EXPOSE 8080

# Run the enhanced chatbot
CMD ["python", "chatbot/app.py"]


