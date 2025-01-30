FROM python:3.11.5

WORKDIR /app

RUN pip install poetry

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false

RUN poetry install --no-root

RUN poetry install

COPY . /app
