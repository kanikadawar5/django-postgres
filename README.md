# django-postgres
Verna Assign
    1. Built the image of django server using docker file
    2. Created docker-compose.yml to provide support for multiple containers
    3. In this docker-compose.yml, 
        - postgresql db is created via postgres image
        - django server is built using docker file
    4. APIs are registered at url -'values'
        
Docker Image sizes are as - 
    826kB - web
    63B - db


Commands to run the project are as - 


1. docker-compose exec postgres psql --user postgres                
2. create database verna_kan_assign;                                #to create db for the user in docker container
3. GRANT ALL PRIVILEGES ON DATABASE verna_kan_assign TO postgres;   #allow user to connect to the db
4. docker-compose up -d --build                                     #build docker images
5.  docker-compose up --remove-orphans                              #both docker containers up - (web/projecct and db/postgres)
