#!/bin/bash

docker run --rm -it -p 8000:8000 -v $PWD/data:/usr/src/data -t javi/platzivolumes
