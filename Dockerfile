FROM ubuntu:latest

MAINTAINER Haisum Mussawir

RUN set -ex \
	&& apt-get update \
	&& apt-get install -y \
 			python-pip \
 			python-dev \
 			build-essential \
 	&& pip install --upgrade pip

ENV APPPATH /opt/myflaskapp
COPY . $APPPATH
WORKDIR $APPPATH/app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["src/app.py"]