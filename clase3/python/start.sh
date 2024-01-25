#!/bin/bash
set -xe

IMAGE=mario21ic/readiness-liveness:v1
CONATINER=demo1

docker build -t $IMAGE ./

echo "Default"
docker run --name=$CONTAINER -d -p 8080:8080 $IMAGE

echo "Wait 6 sec"
sleep 6
curl localhost:8080/live
curl localhost:8080/ready

#docker rm -f $CONTAINER

