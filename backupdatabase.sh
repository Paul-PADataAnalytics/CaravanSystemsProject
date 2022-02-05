#!/bin/bash
tar -czvf /tmp/csppostgresbackup.tar.gz /workspace/.docker-root/volumes/cspdatabase/_data
#upload somehwere
rm /tmp/csppostgresbackup.tar.gz
