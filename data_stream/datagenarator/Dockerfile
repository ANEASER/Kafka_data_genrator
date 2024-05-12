FROM python:3.9-slim

RUN pip install fastapi uvicorn requests

WORKDIR /app

COPY . /app

EXPOSE 5000
CMD ["uvicorn", "datagenarator.data_generator:app", "--host", "0.0.0.0", "--port", "5000"]
