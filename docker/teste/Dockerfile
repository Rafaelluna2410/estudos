FROM maven:3.3-jdk-7 AS build

WORKDIR /opt/app


FROM tomcat:7.0-jre7-alpine

RUN rm -r /usr/local/tomcat/webapps && \
    apk --no-cache add fontconfig ttf-dejavu tzdata

CMD ["catalina.sh", "run"]
