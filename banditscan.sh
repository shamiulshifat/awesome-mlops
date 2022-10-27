#!/bin/sh

# Make sure we are using the latest version
docker pull cytopia/bandit:latest

docker run --rm \
    --volume $(pwd):/data \
    cytopia/bandit:latest \
    -r /data
