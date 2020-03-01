FROM python:3.7.6-stretch

MAINTAINER Haisum Mussawir

ENV APPPATH /opt/myflaskapp
COPY . $APPPATH
WORKDIR $APPPATH/app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["src/app.py"]