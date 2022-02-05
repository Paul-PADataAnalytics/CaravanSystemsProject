#!/bin/bash
export $(grep -v '^#' ~/csp/backend | xargs)
echo "PASSWORD IS:" $POSTGRES_PASSWORD
pgcli -h 127.0.0.1 -p 5432 -U postgres csp 