# blank-telegram-bot
Welcome to the Blank Telegram Bot template, an awesome and efficient way to create async Telegram bots with an Admin panel. This template offers built-in support for multilanguage logic, making it a perfect choice for your next bot development project.

## Tech Stack
This template uses the following technologies:

- [Python](https://www.python.org/)
- [Aiogram](https://docs.aiogram.dev/en/latest/)
- [Sqlalchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [Flask-Admin](https://flask-admin.readthedocs.io/en/latest/)
- [Docker-Compose](https://docs.docker.com/compose/)
- [Redis](https://redis.io/)

## How to run

To start working on this project, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/damhuman/blank-telegram-bot
cd blank-telegram-bot
```

2. Create a .env file in the root directory:
```bash
cp template.env .env
```

3. Replace the TOKEN value in the .env file.

4. To start the bot, run the following command:
```bash
docker-compose up --build -d
```

*Note: On the first run, the bot container will fail because the database for the project hasn't been created yet. You can use the db container (PostgreSQL) to create it, but you can also use any other database for the bot (SQLite/MySQL/MariaDB).*

5. To create the database, run the following commands:
```bash
docker-compose exec db psql -U postgres
```
```SQL
create database bot_db;
create user bot_db_user with password '111';
grant all privileges on database bot_db to bot_db_user;
```
After this step, the DB_URL will be:
```
DB_URL=postgresql://bot_db_user:111@db:5432/bot_db
```

After configuring the database, you can start the bot again using docker-compose:
```bash
docker-compose up --build -d
```

## Admin Panel
This template comes with preconfigured basic logic for the UI Admin panel, which you can find at [http://localhost/admin_panel](http://localhost/admin_panel). It uses Basic Auth logic for login, and you can change the credentials in the .env file.
![image](https://user-images.githubusercontent.com/28063406/235660467-a6d82353-bddc-4469-ad2a-c3871b13b9f0.png)

## Database Migrations
You can use the alembic framework to handle database migrations. To create a migration, use the following command:
```bash
alembic revision --autogenerate -m "Message"
```
Migrations are applied automatically when you run the docker-compose up command. If your table is not parsed via alembic, you have to import it inside the env.py alembic file:

```bash
database/alembic/env.py
```

## Contributing
We welcome pull requests! For major changes, please open an issue first to discuss what you would like to change.

## License
This template is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

## Additional resources
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Aiogram documentation](https://docs.aiogram.dev/en/latest/)
- [Sqlalchemy documentation](https://www.sqlalchemy.org/library.html)
- [Alembic documentation](https://alembic.sqlalchemy.org/en/latest/)
- [Flask-Admin documentation](https://flask-admin.readthedocs.io/en/latest/)
- [Docker-Compose documentation](https://docs.docker.com)
