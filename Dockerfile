# ============================================================================
# Dockerfile do TaskTracker (Fase 3)
#
# A "receita" que o Docker segue para montar a imagem da aplicação. A imagem é
# um pacote pronto, com o Python e o código dentro, que roda igual em qualquer
# computador que tenha o Docker.
#
# Como usar (na pasta onde está este arquivo):
#   docker build -t tasktracker-app .          -> constrói a imagem
#   docker run -it --rm tasktracker-app        -> roda o container
# ============================================================================

# Imagem base: Python 3.11 na versão "slim", que traz só o necessário e por isso
# é menor e mais rápida de baixar do que a imagem completa.
FROM python:3.11-slim

# Pasta de trabalho dentro do container. Os comandos seguintes (COPY e CMD)
# partem daqui, e o Docker cria a pasta se ela não existir.
WORKDIR /app

# Faz o Python mostrar as mensagens na hora, sem guardá-las em um buffer. Em
# container, isso evita que o menu e as perguntas apareçam atrasados no terminal.
ENV PYTHONUNBUFFERED=1

# Copia só a pasta src/ do computador para dentro da imagem. O projeto não tem
# dependências externas, então não é preciso instalar nada com pip.
COPY src/ /app/src/

# Comando executado quando o container inicia: roda o programa. Como é uma
# aplicação interativa, ela precisa ser iniciada com -it (ou pelo Compose).
CMD ["python", "src/main.py"]
