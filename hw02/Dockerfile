FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

COPY ./app /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]