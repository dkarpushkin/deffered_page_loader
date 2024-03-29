FROM python:3.7.4-alpine
WORKDIR /code
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers libxml2-dev libxslt-dev python-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .