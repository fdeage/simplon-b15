# Nothing to install so an alpine image is fine
FROM python:3.11-alpine

WORKDIR /app

COPY . .

EXPOSE 8001

CMD ["python", "-m", "http.server", "8001"]
