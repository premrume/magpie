# magpie

----
## What is magpie
> A magpie is a loud-voiced black and white bird. If someone calls you a magpie, you should probably quiet down. ... You might describe your chatterbox neighbor as a magpie — and the word itself comes from the nickname Mag, short for Margaret and commonly used in slang English to mean "idle chattering."

### Chatter Highlights:
* flask / python
* bootstrap
* docker
* docker-compose
* TODO:  Add ingx or apache ...
* TODO:  Cleanup Network ...

## Prereq's
1. Read thru the CHATTER below 
2. If you want run only go to 'JUST-RUN-IT'
3. If you want the dev point of view  'JUST-DEV-IT'
4. I suggest a clean dedicated linux virtual box VM w/o other docker images ...
5. Gotta have docker and docker-compose installed ... not covered in this doc...

##  CHATTER
----
### Handy docker commands:
    docker rmi --force $(docker images -a -q)
    docker images
    docker ps
### Handy docker-compose commands:
    docker-compose build
    docker-compose up -d
    docker-compose run --rm magpie_web bash
    docker-compose down
----
## JUST-RUN-IT

### 1. Sanity check that you got the tools (sample below)

    [me@localhost magpie]$ docker images
	REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
    [me@localhost magpie]$ docker ps
	CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
    [me@localhost magpie]$ docker volume ls
	DRIVER              VOLUME NAME

### 2. Build (one time deal)

    [me@localhost magpie]$  cd ./magpie
    [me@localhost magpie]$ docker-compose build
    [me@localhost magpie]$ docker images
	REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
	magpie_web          latest              7d4606b04c4a        58 seconds ago      721MB
	magpie_postgres     latest              7347e741192a        2 minutes ago       229MB
	postgres            9.6                 0178d5af9576        41 hours ago        229MB
	python              3.6.1               955d0c3b1bb2        13 months ago       684MB

### 3. Run 
    [me@localhost magpie]$ docker-compose up -d
	Creating network "magpie_magpie" with the default driver
	Creating volume "magpie_data_postgres" with default driver
	Creating volume "magpie_data_images" with default driver
	Creating magpie_postgres_1 ... done
	Creating magpie_web_1      ... done

### 4. Sanity Check
    [me@localhost magpie]$ docker volume ls
	DRIVER              VOLUME NAME
	local               magpie_data_images
	local               magpie_data_postgres
    [me@localhost magpie]$ docker ps
	CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
	12d777163781        magpie_web          "/bin/sh -c 'flask..."   42 seconds ago      Up 41 seconds       0.0.0.0:5000->5000/tcp   magpie_web_1
	768b77ad63a4        magpie_postgres     "docker-entrypoint..."   42 seconds ago      Up 42 seconds       0.0.0.0:5432->5432/tcp   magpie_postgres_1
    
### 5. GOTTA INIT THE DB ONE TIME ...
    [me@localhost magpie]$ docker-compose run --rm web python ./db_create.py
	Starting magpie_postgres_1 ... done
	/usr/local/lib/python3.6/site-packages/psycopg2/__init__.py:144: UserWarning: The psycopg2 wheel package will be renamed from r blah blah blah

### 6. GOTO Web browser and open and cross your fingers:
    http://0.0.0.0:5000
    # test an upload...remember to load a jpg (image)
    
### 7. Shut things down - DO NOT FORGET TO DO THIS
    [me@localhost magpie]$ docker-compose down
    
### 8. Peek at data
     [me@localhost magpie]$ docker volume ls
	DRIVER              VOLUME NAME
	local               magpie_data_images
	local               magpie_data_postgres
	[me@localhost magpie]$ docker inspect magpie_data_images
	[
    	{
        "CreatedAt": "2018-08-24T13:54:02-04:00",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/magpie_data_images/_data",
        "Name": "magpie_data_images",
        "Options": {},
        "Scope": "local"
    }
	]
	[me@localhost magpie]$ sudo ls /var/lib/docker/volumes/magpie_data_images/_data
	[sudo] password for me: 
	images
	[me@localhost magpie]$ sudo ls /var/lib/docker/volumes/magpie_data_images/_data/images
	yourfile.jpg
	
    # if you want to DELETE the data 
    # docker volume prune
        
### 9. Restart
    [me@localhost magpie]$docker-compose up -d
    ... goto browser if you did not prune, data persists
    
----
## JUST-DEV-IT
### 1. Sanity check
    cd <yada>/magpie
    python3 --V  #you got it in path?
### 2. Setup
    cd ./web
    python3 -m virutalenv venv
    # sorry, you will have to go do sudo things for pip install pyscopg ...
    # not enough hours in the day to deal with this:
    #     prolly something like:  pip install pyscopg2
    # but, here is the gist of pip needs:
    pip install --no-cache-dir -r requirements.txt
### 3. Source environment (always)
    . ./web/venv/bin/activate
### 4. Update the users/password (one time deal, opt'l)
    vi ./instance/flask.cfg
    python3 db_create_dockerfile.py
    cd -
### 5. Build & Run (one time deal)
    docker-compose build
    # verify  that you have Magpie's docker images
    docker images
    docker-compose run -d
    docker ps
    # web is the service name in docker-compose.yml
    # do the needful for the db setup
    docker-compose run --rm web python ./db_create.py
### 6. GOTO Web browser and open and cross your fingers:
    http://0.0.0.0:5000
    # test an upload...
### 7. Shut things down - DO NOT FORGET TO DO THIS
    docker-compose down
### 8. Peek at data
    docker volume ls
    docker volume inspect magpie_...
    # if you want to kill it then prune, don't prune to persist
    docker volume prune
### 9. Restart
    docker-compose up -d
### 10.  See your changes live because of the ./web ...
I gotta verify that the above steps are correct... over and out for now... 
