FROM python:3.8-slim

RUN apt-get update -y &&\
    apt-get clean

ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

WORKDIR /service
ADD requirements.txt ./

RUN pip install -r requirements.txt

ADD . /service

EXPOSE 5000
CMD [ "flask", "run", "--host=0.0.0.0" ]
