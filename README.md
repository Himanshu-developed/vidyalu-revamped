# vidyalu_backend
Project Setup

Requirements for setting project to local:-
1- Python3
2- Docker
3- git
4- python virual environment

After Installing above tools follow the Following Commands:-
1- python -m venv venv 

Above command will create a virtual environment that we will be using for development and we will install all the pip requirements
into this environment instead og installing it globally.

2- docker-compose -f .\redis-docker.yaml up -d or make redis-start

it will up container for redis server

3- docker-compose -f .\postgres-docker.yaml up -d or make db-start

it will up database server for application create database with name vidyalu_db

4- python manage.py migrate
 if everything setup correcty it i will start properly without throwing any error.
