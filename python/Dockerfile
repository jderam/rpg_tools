FROM python:3.9

# set working directory and switch to it
WORKDIR /app

# make sure we have gcc which is needed for some of the python packages
# RUN apk add gcc libc-dev python3-dev

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

CMD ["uwsgi", "app.ini"]
