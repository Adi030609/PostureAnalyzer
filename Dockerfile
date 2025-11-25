FROM python:3.10-slim

WORKDIR /app

# Install system dependencies needed for OpenCV & video handling
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
