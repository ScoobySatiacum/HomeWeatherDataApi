#!/bin/bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '[{"barometricpressure":29.766220092773438,"dewpoint":40.0,"heatindex":40.0,"id":13144,"indoorhumidity":38.0,"indoortemperature":72.30000305175781,"outdoorhumidity":99.0,"outdoortemperature":40.29999923706055,"peakwind":2.485485076904297,"rain":27.270000457763672,"timestamp":"1/17/2025 2:36:00 PM","timestampdateonly":"01-16-2025","windaverage":1.2427419424057007,"windchill":40.0,"winddirection":337.5,"windspeed":1.2427419424057007}]' \
  http://127.0.0.1:5000/weather/add
