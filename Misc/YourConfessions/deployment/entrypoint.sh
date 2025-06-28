#!/bin/bash

gunicorn --bind 0.0.0.0:5000 --workers 4 app:app --access-logfile - &

until curl -s http://0.0.0.0:5000/healthcheck >/dev/null; do
  echo "Waiting for app..."
  sleep 1
done

curl -s http://0.0.0.0:5000/signup -X POST -d "username=${USERNAME}&password=${PASSWORD}"  >/dev/null

wait
