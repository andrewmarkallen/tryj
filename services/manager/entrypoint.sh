#!/bin/sh

#build sandbox docker image
cd sandbox
docker build -f /app/sandbox/Dockerfile-sandbox . --tag sandbox:1.0
cd ..

echo "Starting manager"

python3 manage.py run -h 0.0.0.0
