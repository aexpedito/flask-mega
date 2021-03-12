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
