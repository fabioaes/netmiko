FROM python:3.12-slim

WORKDIR /app
ENV PYTHONPATH=/app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia requirements instala
COPY requirements.txt .
COPY ../inventory/ ./inventory/
COPY ../scripts/ ./scripts/
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Comando padrão para iniciar o container em shell interativo
CMD ["bash"]