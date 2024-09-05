ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION} AS builder-image

RUN apt-get update -y \
 && apt-get install -y gcc build-essential  \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN python -m venv /home/app_user/venv
ENV PATH="/home/app_user/venv/bin:$PATH"

RUN pip install poetry
COPY pyproject.toml .
COPY poetry.lock .
RUN poetry config virtualenvs.create false && poetry install --no-root

FROM python:${PYTHON_VERSION} AS runner-image

RUN apt-get update -y \
 && apt-get install -y procps vim  \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN useradd --create-home -g 0 app_user
COPY --from=builder-image --chown=app_user:0 /home/app_user/venv /home/app_user/venv

WORKDIR /home/app_user/code
COPY --chown=app_user:0 . .

# make sure all messages always reach console
ENV PYTHONUNBUFFERED=1

# activate virtual environment
ENV PATH="/home/app_user/venv/bin:$PATH"

RUN poetry config virtualenvs.create false && poetry install

USER app_user
