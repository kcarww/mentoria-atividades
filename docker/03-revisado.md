version: "3.8"

services:
  web:
    build: ./backend
    container_name: django
    ports:
      - "8000:8000"
    env_file:
      - .env
    volumes:
      - ./backend:/app
    depends_on:
      - db

  db:
    image: postgres:16
    container_name: postgres
    environment:
      POSTGRES_DB: ${DB_NAME}
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
