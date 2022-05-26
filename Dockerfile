FROM python:3.9-slim

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN apt-get update \
    && apt-get install -y curl nano \
    && useradd -m app \
    && chown -R app:app /app \
    && pip install --upgrade pip poetry \
    && poetry config virtualenvs.create false \
    && poetry install -v --no-dev

COPY --chown=app . ./

USER app

EXPOSE 8001

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8001", "app.main:app"]
