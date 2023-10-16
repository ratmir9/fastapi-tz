### Запуск проекта с помощью Docker.
1. **Создайте файлы `.env` и `.env.db` для конфигурирования проекта.**
```
touch .env
touch .env.db
```
2. **Откройте файл `.env` и заполните следующими данными.**
```
# server env
SERVER_HOST=0.0.0.0
SERVER_PORT=8000

# env db
DB_USER=fast
DB_PASSWORD=1234QWE 
DB_NAME=short_link
DB_HOST=db
DB_PORT=5432

# env jwt 
JWT_SECRET_KEY=12345-QWERT
JWT_ALGORITHM=HS256

```
3. **Откройте файл `.env.db` и заполните следущими данными.**
```
POSTGRES_USER=fast
POSTGRES_PASSWORD=1234QWE
POSTGRES_DB=short_link
```
**Значение параметров для БД в файлах `.env` и `.env.db` должны совпадать.**

4. **Выполните следующую команду для запуска проекта.**
```
sudo docker-compose up -d
```
5. **Выполните следующую команду для применения миграции.**
```
sudo docker exec -it fast_app alembic upgrade head
```