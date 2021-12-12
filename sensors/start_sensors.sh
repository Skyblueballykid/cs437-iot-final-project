#!/usr/bin/env bash
# stop script on error
set -e
gps_sensor=`ps -eaf | grep -i gps_sensor |sed '/^$/d' | wc -l`
echo $gps_sensor
if [[ $gps_sensor > 1 ]]
then
  echo "gps service is running"
else
  echo "gps service not running starting"
  nohup python3 /home/pi/cs437-iot-final-project/sensors/gps_sensor.py &
fi

wind_sensor=`ps -eaf | grep -i wind_sensor |sed '/^$/d' | wc -l`
echo $wind_sensor
if [[ $wind_sensor > 1 ]]
then
  echo "wind service is running"
else
  echo "wind service not running starting"
  nohup python3 /home/pi/cs437-iot-final-project/sensors/wind_sensor.py &
fi

temp_sensor=`ps -eaf | grep -i temp_sensor |sed '/^$/d' | wc -l`
echo $temp_sensor
if [[ $temp_sensor > 1 ]]
then
  echo "Temperature and humidity service is running"
else
  echo "Temperature and humidity not running starting"
  nohup python3 /home/pi/cs437-iot-final-project/sensors/temp_sensor.py &
fi

upload_historical=`ps -eaf | grep -i upload_historical |sed '/^$/d' | wc -l`
echo $upload_historical
if [[ $upload_historical > 1 ]]
then
  echo "Historical upload service is running"
else
  echo "Historical upload service not running starting"
  nohup python3 /home/pi/cs437-iot-final-project/sensors/upload_historical.py &
fi