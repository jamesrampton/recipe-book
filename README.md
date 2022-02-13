# Setup

`docker volume create recipe_book_media`

`docker volume create recipe_book_db`

`echo "SECRET_KEY='supersecret'" >> .env`
`echo "POSTGRES_NAME='db_name'" >> .env`
`echo "POSTGRES_USER='db_user'" >> .env`
`echo "POSTGRES_PASSWORD='db_password'" >> .env`

`docker-compose build`

`docker-compose up`
