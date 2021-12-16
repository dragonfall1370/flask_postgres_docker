FROM python:3.7.12-bullseye

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN apt-get update \
    && apt-get -y install libpq-dev gcc
    # && pip install psycopg2
# RUN apt add --no-cache gcc musl-dev linux-headers
COPY . /app
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "run"]