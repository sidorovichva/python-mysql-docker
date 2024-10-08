FROM    python:3.12-slim-bullseye

LABEL   author="Adam Sidorovich"

WORKDIR /app

RUN     apt-get update && apt-get install -y curl
RUN     curl -sSL https://install.python-poetry.org | python3 -

ENV     PATH="/root/.local/bin:$PATH"
ENV     HOST=localhost
ENV     PORT=8099
ENV     USERNAME=root
ENV     PASSWORD=pw
ENV     DATABASE=projects

COPY    . /app

RUN     poetry install --no-dev

EXPOSE  $PORT

CMD     ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8099"]
