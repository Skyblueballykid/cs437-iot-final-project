from gpsdclient import GPSDClient
import argparse
import json
import datetime

FILE_NAME = "gps-telemetry.json"


class GPSSensor:
    def __init__(self, timestamp, gps_latitude, gps_longitude):
        self.timestamp = timestamp
        self.gps_latitude = gps_latitude
        self.gps_longitude = gps_longitude

    def __rep__(self):
        return self.__dict__


def write_file(json_dumped: str, file_name: str):
    with open(file_name, "w") as file_handle:
        file_handle.write(json_dumped)


def main():
    host = args.host
    data_path = args.data_path
    client = GPSDClient(host=host)
    for gps_data in client.dict_stream(convert_datetime=False):
        if gps_data["class"] == "TPV":
            gps_sensor = GPSSensor(
                timestamp=str(datetime.datetime.now())[:16],
                gps_latitude=gps_data.get("lat", "n/a"),
                gps_longitude=gps_data.get("lon", "n/a"),
            )
            json_dumped = json.dumps([gps_sensor.__rep__()])
            write_file(json_dumped, data_path + FILE_NAME)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data-path",
        type=str,
        required=False,
        help="path to write data files",
        default="/home/pi/gps-data/",
    )
    parser.add_argument(
        "--host",
        type=str,
        required=False,
        help="host address",
        default="0.0.0.0",
    )
    args = parser.parse_args()
    main()
