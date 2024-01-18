# DRF Project with Docker Compose

This is a Django REST Framework (DRF) project that uses Docker Compose to set up a development environment with a MySQL database.

## Prerequisites

Before you start, make sure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/vashchukvlad/drf-owu
cd drf-owu
```

### 2. Configure Environment

Edit the configuration of the mysql db in settings.py and .env.mysql

### 3. Run MySql Docker Container

```bash
docker compose up
```

### 4. Run Server

```
python manage.py runserver
```
