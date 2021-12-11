#!/usr/bin/env python3

import time
import json
import datetime
import argparse
import serial

FILE_NAME = "wind-telemetry.json"
TIMEOUT = 1


class WindSensor:
    def __init__(self, timestamp, wind_speed):
        self.timestamp = timestamp
        self.wind_speed = wind_speed

    def __rep__(self):
        return self.__dict__


def write_file(json_dumped: str, file_name: str):
    with open(file_name, "w") as file_handle:
        file_handle.write(json_dumped)


def main():
    data_path = args.data_path
    serial_name = "/dev/ttyACM0"
    baud_rate = 9600
    timeout = 10
    while True:
        with serial.Serial(serial_name, baud_rate, timeout=TIMEOUT) as ser:
            arduino_serial_out = ser.readline().decode("utf-8")
            if arduino_serial_out:
                wind_sensor = WindSensor(
                    timestamp=str(datetime.datetime.now())[:16],
                    wind_speed=arduino_serial_out.strip(),
                )
                json_dumped = json.dumps([wind_sensor.__rep__()])
                write_file(json_dumped, data_path + FILE_NAME)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data-path",
        type=str,
        required=False,
        help="path to write data files",
        default="/home/pi/wind-data/",
    )
    args = parser.parse_args()
    main()
