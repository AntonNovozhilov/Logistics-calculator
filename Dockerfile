FROM python:3.11
WORKDIR /app
COPY pyproject.toml .
COPY poetry.lock .
RUN pip install poetry
RUN poetry install --no-root
COPY . .
CMD ["poetry", "run", "python", "-m", "app.main"]
