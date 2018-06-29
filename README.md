# Django y Celery en contenedores de Docker, para dev y producción
## 2018-06-28

Docker es una manera de empaquetar tu sistema operativo, dependencias y código de una manera replicable y consistente.

Empaquetas estas dependencias en __images__. Un Docker image es un archivo que usas para crear contenedores (instancias de images) que corren tu código.

Puedes deployar tu código a producción usando estas imágenes. También puedes combinar images, incluso images hechos por otros, para crear tu ambiente de ejecución más fácilmente.


## Ventajas
- No necesita un "Guest OS": usa poca memoria en comparación con una VM
  + también usa poco disco!
- Fácil de replicar y controlar ambiente de ejecución
- Fácil de compartir con otros miembros de tu equipo
- Puedes usar los mismos `Dockerfile`s para hacer tus imágenes de desarrollo y producción
  + los ambientes son tan parecidos que ya ni tengo ambiente de staging!

![Docker vs VM](https://www.researchgate.net/profile/Ling-Hong_Hung/publication/299771559/figure/fig4/AS:359778707623937@1462789336136/A-comparison-of-the-architecture-of-virtual-machines-and-Docker-software.png)


## Preparación
### Para OSX
- Instalar [Docker](https://store.docker.com/editions/community/docker-ce-desktop-mac)
- Instalar Python 3.6 (`brew install python3`)


## Helpers
~~~sh
alias dkp='docker ps'
alias dk='docker-compose'

dkash () {
  docker exec -it $1 /bin/ash
}

dksh () {
  docker exec -it $1 /bin/bash
}
~~~


## Temas
- `Dockerfile`s
- `docker-compose.yml`
- '`dev.sh`'
- '`build.sh`'
- AWS: `Dockerrun.aws.json` (usando imágenes hechas de los mismos Dockerfiles)
