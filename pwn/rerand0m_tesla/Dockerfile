FROM ubuntu
RUN apt update -y
RUN apt install -y tcpd xinetd
RUN useradd tesla
RUN echo "tesla 778/tcp" >> /etc/services
COPY config /etc/xinetd.d/tesla
COPY tesla /tesla
COPY flag /flag
CMD xinetd -dontfork
