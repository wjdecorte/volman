FROM python:3.12-slim

RUN apt-get update -y \
    && apt-get install -y gcc build-essential procps vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /home/app_user/code

RUN useradd --create-home -g 0 app_user

# RUN python -m venv /home/app_user/venv
# ENV PATH="/home/app_user/venv/bin:$PATH"

RUN pip install poetry
COPY --chown=app_user:0 . .
RUN poetry config virtualenvs.create false && poetry install


# make sure all messages always reach console
ENV PYTHONUNBUFFERED=1

USER app_user
