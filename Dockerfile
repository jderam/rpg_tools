FROM python:3.8.9-alpine

WORKDIR /app

# make sure we have gcc which is needed for some of the pytohn packages
# RUN apk add build-base
RUN apk add gcc libc-dev

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
