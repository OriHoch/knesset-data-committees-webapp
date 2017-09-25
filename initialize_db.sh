#!/usr/bin/env bash

docker-compose up -d --build db
sleep 5
docker-compose exec db sh -c "cat /db_dump.sql | su-exec postgres psql"
