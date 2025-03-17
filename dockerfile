FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy required files
COPY requirements.txt requirements.txt
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for Streamlit
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "cryptography_1.py", "--server.port=8501", "--server.address=0.0.0.0"]
