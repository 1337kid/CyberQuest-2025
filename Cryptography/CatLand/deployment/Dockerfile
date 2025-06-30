FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install pytz wonderwords
COPY server.py .

EXPOSE 12345

CMD ["python", "server.py"]