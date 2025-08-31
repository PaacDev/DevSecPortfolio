# DevSecPortfolio - Sensor Dashboard

Este proyecto es un **dashboard de sensores** desarrollado en Django, que visualiza temperatura, humedad y consumo de energía en gráficos interactivos usando Chart.js y Bootstrap.

El proyecto está preparado para ejecutarse con **Docker y Docker Compose**, lo que garantiza un entorno reproducible y limpio sin necesidad de instalar Python o dependencias localmente.

---

## Tecnologías

- Python 3.11
- Django 5.2.5
- Bootstrap 5
- Chart.js
- Docker / Docker Compose
- SQLite (base de datos por defecto)

---

## Instalación y uso con Docker Compose

1. Clonar el repositorio:

```bash
git clone https://github.com/tu_usuario/DevSecPortfolio.git
cd DevSecPortfolio
```

2. Construir y levantar el contenedor:
```bash
docker-compose up --build
```
3. Abrir en el navegador:

http://127.0.0.1:8000/

Todos los cambios en el código local se reflejarán automáticamente gracias al volumen montado en Docker Compose.

4. Para detener el contenedor:
```bash
docker-compose down
```

## Ejecutar Test
Puedes correr los tests de Django dentro del contenedor:
```bash
docker-compose run web python manage.py test
```
