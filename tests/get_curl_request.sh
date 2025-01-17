#!/bin/bash
curl --header "Content-Type: application/json" \
  --request GET \
  http://127.0.0.1:5000/weather/current
