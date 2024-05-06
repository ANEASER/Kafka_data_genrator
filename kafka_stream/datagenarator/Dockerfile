FROM python:3.9-slim

RUN pip install Flask gunicorn

WORKDIR /app

COPY . /app

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "data_generator:app"]
