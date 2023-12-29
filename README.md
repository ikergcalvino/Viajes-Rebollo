# Viajes Rebollo

## Integrantes

- **Álvaro Díaz Díaz:** *alvaro.ddiaz@udc.es*
- **Iago Domínguez Cameán:** *iago.dominguez.camean@udc.es*
- **Iker García Calviño:** *iker.gcalvino@udc.es*
- **Dennimar Gil Ortega:** *d.gortega@udc.es*
- **Joel Sánchez Rúas:** *joel.sanchez.ruas@udc.es*
- **Juan Toirán Freire:** *juan.tfreire@udc.es*

## Cómo ejecutar

### En local

Para ejecutar en local, necesitaremos tener instalado Python 3 (desarrollo realizado en Python 3.12.1) y los módulos indicados en el fichero `requirements/requirements.txt`:

```
pip install -r requirements/requirements.txt
```

Una vez instalado, podemos ejecutar el script de arranque `start.sh` o bien ejecutar los siguientes comandos manualmente:

``` bash
python viajesrebollo/manage.py makemigrations
python viajesrebollo/manage.py migrate
python viajesrebollo/manage.py runserver 0.0.0.0:8000
```

### En Docker

Para ejecutar la web, debemos tener instalado el servidor de despliegue de [Docker](https://www.docker.com/).

Una vez instalado, podemos ejecutar Docker desde Visual Studio Code:

```
> Dev Containers: Rebuild and Reopen in Container
```

Dentro del contenedor, podemos ejecutar el siguiente script por primera vez para arrancar el servidor:

```
bash script.sh
```
