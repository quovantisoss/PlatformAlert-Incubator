FROM alpine:latest
MAINTAINER Abhishek Shukla
RUN apk --no-cache --update-cache add dumb-init python3 python3-dev 
RUN easy_install-3.6 -U pip

RUN mkdir /opt
RUN addgroup -S application
RUN adduser -S application -G application -h /opt/apps -s /bin/sh 
RUN pip install virtualenv
RUN virtualenv -p /usr/bin/python3  /opt/apps/venv

COPY . /opt/apps/platformalert
RUN /opt/apps/venv/bin/pip install -r /opt/apps/platformalert/py-requirements/dev.txt

ENTRYPOINT ["dumb-init", "/opt/apps/venv/bin/python", "manage.py"]


## Building Image
## docker build -t platformalert:latest .

## Running the container
## docker run -w /opt/apps/platformalert -p 5000:5000 -it platformalert:latest /bin/sh