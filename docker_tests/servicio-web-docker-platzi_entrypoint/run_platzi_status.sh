#!/bin/bash

### ERROR:Theoretically, this is the way of launching this service, but it return err111 (Connection refused).

docker run --net=host --rm -it javi/platzistatus 1
# docker run --net=host --rm -it javi/platzistatus
