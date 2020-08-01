#!/bin/bash

service nginx start

trap exit TERM
while :; do
  echo "Restarting nginx..."
  service nginx restart
  echo "...nginx restarted, sleeping 6 hours."
  sleep 6h
done
