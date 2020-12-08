#!/bin/bash

### We should send CURLs to localhost:8000 (80 is just an internal port)
docker run --rm -p 8000:80 -it -v $PWD/data/src/data javi/platziws1

### We could change the port depending on OS environment variables:

# export PORT=3333

## With option -e we are saying that our container should set up its variable PORT with the value of the environment variable PORT

# docker run --rm -it -p 8000:$PORT -e PORT=$PORT -v $PWD/data/src/data  javi/platziws1

