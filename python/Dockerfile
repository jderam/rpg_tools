FROM python:3.10-slim-bullseye

# set working directory and switch to it
WORKDIR /app

# make sure we have gcc which is needed to install uwsgi
RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip setuptools wheel

RUN pip install -r requirements.txt

COPY . .

RUN python setup.py sdist bdist_wheel

RUN pip install dist/rpg_tools-*-py3-none-any.whl

CMD ["uwsgi", "app.ini"]
