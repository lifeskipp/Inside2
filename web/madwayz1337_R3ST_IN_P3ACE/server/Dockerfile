FROM python:3.7-alpine

WORKDIR /src

COPY src .
COPY requirements.txt .

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt --no-cache-dir

ENV FLASK_APP=__init__.py
ENV FLAG="ELON{46945a829bcdbebfe89f8fb5b9c50865}"

EXPOSE 7777

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "7777"]


