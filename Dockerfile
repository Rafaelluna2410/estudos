FROM ubuntu

EXPOSE 80

RUN apt update && apt install update  && apt install -y apache2 
RUN apt-get install systemd -y


