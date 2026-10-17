# Empacotamento do TaskTracker em container (previsto para a Fase 3).
# Como usar (a aplicação é interativa, por isso o -it):
#   docker build -t tasktracker .
#   docker run -it tasktracker
FROM python:3.12-slim
WORKDIR /app
COPY src/ ./src/
CMD ["python", "src/main.py"]
