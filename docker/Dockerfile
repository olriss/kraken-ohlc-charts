# Base image: Uygulamanızın Python sürümüne uygun bir imaj seçin
FROM python:3.11-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Gereksinimler dosyasını kopyala
COPY requirements.txt requirements.txt

# Bağımlılıkları yükle
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu kopyala
COPY . .

# Expose the port used by Prometheus exporter (örneğin 8000)
EXPOSE 8000

# Container çalıştırıldığında başlatılacak komut
CMD ["python", "ohlc_exporter.py"]
