#!/bin/bash

### -d: detached mode (background)

docker run --rm  -dit -p 8000:80 -v $PWD/data/src/data javi/platziws1

### This returns an id. If we want to have this container in foreground, we could execute:
# docker attach <id>
### To stop:
# docker stop <id>
### To enter the container (command could be "bash", for instance):
# docker exec -it <id> <command>

### Work with ids could be a bit annoying, so we can name our containers:
# docker run -dit -p8000:80 -v $PWD/data/src/data --name my_docker_container javi/platziws1
