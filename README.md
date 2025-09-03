# DevSecPortfolio - Sensor Dashboard
[![SonarQube Cloud](https://sonarcloud.io/images/project_badges/sonarcloud-light.svg)](https://sonarcloud.io/summary/new_code?id=PaacDev_DevSecPortfolio)

[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=PaacDev_DevSecPortfolio&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=PaacDev_DevSecPortfolio)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=PaacDev_DevSecPortfolio&metric=bugs)](https://sonarcloud.io/summary/new_code?id=PaacDev_DevSecPortfolio)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=PaacDev_DevSecPortfolio&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=PaacDev_DevSecPortfolio)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=PaacDev_DevSecPortfolio&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=PaacDev_DevSecPortfolio)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=PaacDev_DevSecPortfolio&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=PaacDev_DevSecPortfolio)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=PaacDev_DevSecPortfolio&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=PaacDev_DevSecPortfolio)

Este proyecto es un **dashboard de sensores** desarrollado en Django, que visualiza temperatura, humedad y consumo de energía en gráficos interactivos usando Chart.js y Bootstrap.

El proyecto está preparado para ejecutarse con **Docker y Docker Compose**, usando **PostgreSQL** como base de datos, lo que garantiza un entorno reproducible y limpio sin necesidad de instalar Python o dependencias localmente.

---

## Tecnologías

- Python 3.11
- Django 5.2.5
- Bootstrap 5
- Chart.js
- PostgreSQL 15
- Docker / Docker Compose

---

## Instalación y uso con Docker Compose

### 1. Clonar el repositorio:

```bash
git clone https://github.com/tu_usuario/DevSecPortfolio.git
cd DevSecPortfolio
```

### 2. Configuración del entorno:

Copia el archivo .env.example a .env:

macOS/Linux
```bash
cp .env.example .env
```
Windows (CMD):
```bash
copy .env.example .env
```

### 3. Construir y levantar el contenedor:

```bash
docker-compose up --build
```

### 4.  Cargar datos de ejemplo en el modelo SensorData: 

```bash   
docker-compose run web python manage.py runscript generate_data
```

### 5. Abrir en el navegador:

http://127.0.0.1:8000/

*Todos los cambios en el código local se reflejarán automáticamente gracias al volumen montado en Docker Compose.*

### 6. Para detener el contenedor:

```bash
docker-compose down
```

## Ejecutar Test
Puedes correr los tests de Django dentro del contenedor:
```bash
docker-compose run web python manage.py test
```
