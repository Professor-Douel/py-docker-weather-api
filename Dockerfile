FROM python:3.11.11-alpine3.19
LABEL maintainer="imtence@gmail.com"

ENV PYTHONBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app/ /app/

CMD ["python", "main.py"]
