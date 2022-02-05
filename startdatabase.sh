#!/bin/bash
if [ $1 = "create" ]; then
	docker build --tag cspdatabase:latest cspbackend
	docker volume create cspdatabase
fi
if [ $1 = "restart" ]; then
	docker rm cspdatabase
fi
docker run -d -v cspdatabase:/var/lib/postgresql/data --name cspdatabase --env-file ~/csp/backend -p 5432:5432 cspbackend:latest
