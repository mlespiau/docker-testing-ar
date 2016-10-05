FROM alpine:3.4

RUN apk update && \
        apk add py-pip=8.1.2-r0 && \
        pip install Flask

ADD app.py /app/app.py

EXPOSE 5000

ENTRYPOINT ["python", "/app/app.py"]
