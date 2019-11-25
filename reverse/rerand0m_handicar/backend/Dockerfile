FROM ubuntu
RUN apt update -y
RUN apt install -y tcpd xinetd
RUN useradd handicar
RUN echo "handicar 1778/tcp" >> /etc/services
COPY config /etc/xinetd.d/handicar
COPY backend /handicar
COPY db /db
COPY mil /mil
RUN chmod 666 db
RUN chmod 666 mil
CMD xinetd -dontfork
