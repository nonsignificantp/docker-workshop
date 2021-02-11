# Docker-workshop

## Instalacion

Primer paso: Seguir la guia de instalacion de docker: https://docs.docker.com/engine/install/ubuntu/

Segundo paso: Seguir la guia de instalacion de docker-compose: https://docs.docker.com/compose/install/

Tercer paso: remover `sudo` para el uso del comando `docker` y `docker-compose`: https://docs.docker.com/engine/install/linux-postinstall/

## Uso del repositorio

### Levantar el ambiente de desarrollo

Dentro de `docker-compose.yml` se encuentran las instrucciones para levantar un ambiente de desarrollo que contenga jupyter-notebook, postgresql y pgadmin4. Para levantar el ambiende debemos pararnos en la carpeta raiz del proyecto (donde se encuentra el README.md) y ejecutar la siguiente instruccion en la terminal.

```
docker-compose up
```

Una vez que terminamos podemos cerrar el ambiente con `ctrl-c` en la terminal donde se esta ejecutando o en una terminal ingresar:

```
docker-compose stop
```

### Levantar airflow

Dentro de la carpeta `airflow/` ejecutamos:

```
docker build -y myAirflow .
```

Una vez terminado instanciamos el container a partir de la imagen:

```
docker run -p 8080:8080 myAirflow
```

Por ultimo vamos al navegador e ingresamos en `http://localhost:8080`.

### Levantar api

Dentro de la carpeta `api/` ejecutamos:

```
docker build -y myAPI .
```

Una vez terminado instanciamos el container a partir de la imagen:

```
docker run -p 80:80 myAPI0
```

Por ultimo vamos al navegador e ingresamos en `http://localhost:80`.