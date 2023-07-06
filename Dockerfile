FROM python:3.8

RUN mkdir -p /usr/scr/app/
WORKDIR /usr/scr/app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /usr/scr/app/

RUN apt-get update
RUN apt-get -y install postgresql-client

RUN chmod +x entrypoint.sh

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["entrypoint.sh"]
