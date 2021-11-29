#!/bin/bash

docker network create mongo-network

docker run --name mongodb \
--network mongo-network \
-e MONGO_INITDB_ROOT_USERNAME=root \
-e MONGO_INITDB_ROOT_PASSWORD=root \
-v /path/to/mongodb:/data/db \
-p 127.0.0.1:27017:27017 \
-d \
mongo:latest

docker run --name mongo-express \
--network mongo-network \
-e ME_CONFIG_MONGODB_SERVER=mongodb \
-e ME_CONFIG_MONGODB_ADMINUSERNAME=root \
-e ME_CONFIG_MONGODB_ADMINPASSWORD=root \
-e ME_CONFIG_BASICAUTH_USERNAME=root \
-e ME_CONFIG_BASICAUTH_PASSWORD=root \
-p 127.0.0.1:8081:8081 \
-d \
mongo-express:latest

