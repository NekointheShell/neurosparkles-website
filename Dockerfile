FROM debian


ENV DEBIAN_FRONTEND noninteractive
RUN apt update
RUN apt install -y gunicorn python3 python3-pip


ADD . /website
RUN cd /website; pip install .


CMD gunicorn website:app
