# Imagem do TaskTracker: leve e autossuficiente (Fase 3).

# Base leve do sistema, só com o Python 3.11.
FROM python:3.11-slim

# Pasta central de operações dentro do container.
WORKDIR /app

# Garante a saída imediata de mensagens no terminal (sem buffer).
ENV PYTHONUNBUFFERED=1

# Injeta o código local no container.
COPY src/ /app/src/

# Gatilho que dispara a execução da aplicação.
CMD ["python", "src/main.py"]
