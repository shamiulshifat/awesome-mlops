#!/bin/sh

SRC_DIRECTORY="$(pwd)"
REPORT_DIRECTORY="$SRC_DIRECTORY/report"

if [ ! -d "$REPORT_DIRECTORY" ]; then
    echo "Initially creating persistent directories"
    mkdir -p "$REPORT_DIRECTORY"
    chmod -R 777 "$REPORT_DIRECTORY"
fi

# Make sure we are using the latest version
docker pull cytopia/bandit:latest

docker run --rm \
    --volume $(pwd):/data \
    --volume "$REPORT_DIRECTORY":/data \
    cytopia/bandit:latest \
    -r /data
