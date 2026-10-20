# Repaso DevOps: Docker, Flask & GitHub Actions (CI/CD)

Proyecto práctico de una API en Python (Flask) contenerizada con Docker y automatizada mediante un pipeline de CI/CD con GitHub Actions.

## Estructura del Proyecto

```text
├── .github/
│   └── workflows/
│       └── ci-cd.yml       # Pipeline automatizado de CI/CD
├── .dockerignore           # Archivos excluidos de la imagen Docker
├── Dockerfile              # Definición de la imagen del contenedor
├── app.py                  # Servidor Flask básico (puerto 5000)
├── test_app.py             # Pruebas unitarias automatizadas
├── requirements.txt        # Dependencias del proyecto
└── README.md
```

## Pipeline de CI/CD (GitHub Actions)

El flujo `.github/workflows/ci-cd.yml` se ejecuta automáticamente en cada `push` o `pull_request` a la rama `main`:

1. **CI (Continuous Integration) - Lint & Tests**:
   - Descarga el código y configura Python 3.12.
   - Instala las dependencias y analiza sintaxis con `flake8`.
   - Ejecuta las pruebas unitarias con `pytest test_app.py`.

2. **Docker Build & Smoke Test**:
   - Construye la imagen de Docker a partir del `Dockerfile`.
   - Levanta el contenedor de prueba y verifica con `curl` que el endpoint responde `200 OK`.

3. **CD (Continuous Delivery) - Publicación en GHCR**:
   - Se ejecuta únicamente en la rama `main` tras pasar las etapas anteriores.
   - Construye y publica automáticamente la imagen en GitHub Container Registry (`ghcr.io`).

## Cómo probar localmente

### 1. Pruebas unitarias
```bash
pip install -r requirements.txt
pytest test_app.py -v
```

### 2. Construir y correr con Docker
```bash
docker build -t mi-app-docker .
docker run -d -p 5000:5000 --name mi-contenedor mi-app-docker
```
Acceder a [http://localhost:5000/](http://localhost:5000/) en el navegador o terminal.
