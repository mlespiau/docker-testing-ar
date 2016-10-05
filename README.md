# docker-testing-ar
Repo con el código usado para las demo de TestingAR meetup.

# Demo 1
Steps:
```bash
$ cd demo1
$ nano Dockerfile
```

Review Dockerfile
```bash
$ docker run -p 5000:5000 testing-ar:0.1
$ docker run
```
Load http://127.0.0.1:5000/ - PROFIT
```bash
$ docker ps
```
Review port mappings. Need to expose the port in the docker host.
