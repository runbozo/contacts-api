# syntax=docker/dockerfile:experimental
FROM python:3.9

WORKDIR /contacts-api
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.1.12

RUN pip install "poetry==$POETRY_VERSION"
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock /contacts-api/

RUN poetry install --no-dev

COPY app /contacts-api/app/
COPY config.py /contacts-api/

RUN poetry run flask db init && \
    poetry run flask db migrate -m "contacts table" && \
    poetry run flask db upgrade

ENV FLASK_APP=app

CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0", "--port=8080"]
