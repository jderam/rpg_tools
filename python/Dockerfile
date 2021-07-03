FROM python:3.9.6-slim-buster

# set working directory and switch to it
WORKDIR /app

# make sure we have gcc which is needed for some of the python packages
# RUN apk add gcc libc-dev python3-dev
RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

CMD ["uwsgi", "app.ini"]
