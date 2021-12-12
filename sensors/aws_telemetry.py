#!/usr/bin/env python3

import time
import json
import datetime
import argparse
import boto3

FILE_NAME = "telemetry.json"
TIMEOUT = 60


class AWSTelemetry:
    def __init__(
            self,
            timestamp,
            temperature_fahrenheit,
            humidity,
            wind_mph,
            gps_latitude,
            gps_longitude,
    ):
        self.timestamp = timestamp
        self.temperature_fahrenheit = temperature_fahrenheit
        self.humidity = humidity
        self.wind_mph = wind_mph
        self.gps_latitude = gps_latitude
        self.gps_longitude = gps_longitude

    def __rep__(self):
        return self.__dict__


def write_file(json_dumped: str, file_name: str):
    with open(file_name, "w") as file_handle:
        file_handle.write(json_dumped)


def open_file(file_name: str) -> dict:
    with open(file_name, "r") as fh:
        s = fh.read()
    return json.loads(s)


def s3_upload(file_name: str, bucket_name: str, object_name: str):
    s3 = boto3.client("s3")
    with open(file_name, "rb") as fh:
        s3.put_object(
            Bucket=bucket_name,
            Key=object_name,
            Body=fh,
            ContentType="application/json",
            ACL="public-read",
        )


def main():
    data_path = args.data_path
    while True:
        try:
            # load data from Temperature Service
            temp_file = "/home/pi/temphumidity-data/temp-telemetry.json"
            temp_dict = open_file(temp_file)[0]
            temperature_fahrenheit = round(temp_dict.get("temperature_fahrenheit", ""))
            humidity = round(temp_dict.get("humidity", ""))

            # load data from Wind Service
            wind_file = "/home/pi/wind-data/wind-telemetry.json"
            wind_dict = open_file(wind_file)[0]
            wind_mph = round(float(wind_dict.get("wind_speed", "")))

            # load data from GPS service
            gps_file = "/home/pi/gps-data/gps-telemetry.json"
            gps_dict = open_file(gps_file)[0]
            gps_latitude = gps_dict.get("gps_latitude", "")
            gps_longitude = gps_dict.get("gps_longitude", "")

            timestamp = str(datetime.datetime.now())[:16]

            aws_telemetry = AWSTelemetry(
                timestamp=timestamp,
                temperature_fahrenheit=temperature_fahrenheit,
                humidity=humidity,
                wind_mph=wind_mph,
                gps_latitude=gps_latitude,
                gps_longitude=gps_longitude,
            )

            json_dumped = json.dumps([aws_telemetry.__rep__()], indent=4)
            print(json_dumped)
            write_file(json_dumped, data_path + FILE_NAME)
            s3_upload(
                file_name=data_path + FILE_NAME,
                bucket_name="telemetry-dropoff",
                object_name="telemetry.json",
            )
        except Exception as err:
            print(str(err))

        time.sleep(TIMEOUT)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data-path",
        type=str,
        required=False,
        help="path to write data files",
        default="/home/pi/aws-data/",
    )
    args = parser.parse_args()
    main()
