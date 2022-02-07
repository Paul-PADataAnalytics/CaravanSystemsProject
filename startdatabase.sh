#!/bin/bash
if [ -z ${1+x} ]; then
	echo "startdatabase.sh create|restart|onlystart"
	exit 1
fi
if [ $1 = "create" ]; then
	docker build --tag cspdatabase:latest csp-backend
	docker volume create cspdatabase
	docker run -d -v cspdatabase:/var/lib/postgresql/data --name cspdatabase --env-file ~/csp/backend -p 5432:5432 cspbackend:latest
fi
if [ $1 = "restart" ]; then
	docker rm cspdatabase
fi
docker start cspdatabase