FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry

COPY . .

RUN poetry config virtualenvs.create false && poetry install --no-root

CMD ["uvicorn", "fast_deploy.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
