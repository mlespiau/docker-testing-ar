FROM alpine:3.4

ADD . /app/

WORKDIR /app/

RUN apk update && \
        apk add py-pip=8.1.2-r0 && \
        pip install -r requirements.txt

ENTRYPOINT ["python", "/app/app.py"]
