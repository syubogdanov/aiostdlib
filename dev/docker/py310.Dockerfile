FROM python:3.10-slim-bullseye

WORKDIR /aiostdlib

RUN apt-get update \
    && apt-get install --no-install-recommends --yes make \
    && apt-get clean

COPY pyproject.toml ./

RUN python -m pip install --no-cache-dir poetry==1.8.4 \
    && poetry config virtualenvs.create false \
    && poetry install --no-ansi --no-interaction --with lint,test

COPY ./ ./

ENTRYPOINT [ "python" ]
CMD [ "--help" ]
