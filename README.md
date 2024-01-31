
# Data Engineering Zoomcamp 2024 - Homework 2

## Instructions

1. Create Docker/Postgres data folder:

```console
mkdir -p data/postgres
```
2. Start Docker:

```console
docker compose -f docker/docker-compose.yaml up -d
```

3. Open Mage

Open the browser, go to the local [Mage - http://localhost:6789](http://localhost:6789), and check the Pipelines and Triggers pages

4. Questions  
Please check the [Homework Execution](./homework_execution.md) document.

5. Stop Docker

```console
docker compose -f docker/docker-compose.yaml down -v
```