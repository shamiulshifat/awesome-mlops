#!/bin/sh
set +e
# Make sure we are using the latest version
docker pull hysnsec/bandit:latest

docker run --rm \
    --volume $(pwd):/data \
    hysnsec/bandit:latest \
    -r /data
 
set +e
