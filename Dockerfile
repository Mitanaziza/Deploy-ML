# Gunakan base image Python
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Salin semua file ke dalam container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (hanya untuk dokumentasi, Cloud Run mengabaikan ini)
EXPOSE 8080

# Jalankan aplikasi menggunakan uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
