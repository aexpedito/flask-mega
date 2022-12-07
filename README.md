# create virtual env
$ python -m venv venv



# upgrade pip and setuptools if needed
$ python -m pip install -U pip
$ pip install --upgrade setuptools

#
set DOCKER_BUILDKIT=0
set COMPOSE_DOCKER_CLI_BUILD=0

docker build -t indecision_app .

#compose
$ docker-compose up 
$ docker-compose up --build


docker run -d --rm -p 5432:5432 -v C:\Users\afonsoe\Documents\pessoal\scripts\git-projects\flask-mega\postgres\data:/var/lib/postgresql/data local_postgres_flask_mega:1.0