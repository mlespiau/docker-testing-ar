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

# Demo 2
Explicar OpenCATS.

Explicar que vamos a hacer:
- Correr un conjunto de contenedores que definen el entorno de testing de OpenCATS + Tools de testing (Selenium)
- Ejecutar tests automaticos

```bash
$ git clone https://github.com/opencats/OpenCATS.git
$ cd OpenCATS/docker
```

Ver docker-compose-test.yml

```bash
$ docker-compose -f docker-compose-test.yml up
```

Chequear la aplicación.

```bash
$ docker ps
```
Ver tests/runAllTests.sh

```bash
$ docker exec -it {containerID} /var/www/public/test/runAllTests.sh
```
