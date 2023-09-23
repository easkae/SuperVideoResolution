Tested on windows 10.

Requirements:

Anaconda, docker

How to run:

1)create docker container

docker build -t SVR .

docker run -it SVR

2)check docker container id with:

docker ps

3)go into container:

docker exec -it <container_id from pt 2> /bin/bash
