FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_ROOT_USER_ACTION ignore

RUN mkdir -p /usr/scr/app/
WORKDIR /usr/scr/app/

COPY . /usr/scr/app/

RUN apt-get update
RUN #apt-get -y install apt-utils
RUN apt-get -y install postgresql-client

RUN chmod +x entrypoint.sh

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["entrypoint.sh"]
