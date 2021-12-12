#!/usr/bin/env python3

import json
import boto3
import time

HISTORICAL_FILE_NAME = "/home/pi/aws-data/historical/telemetry.json"
SLEEP_TIME = 600

def main():
    while True:
        s3 = boto3.client("s3")
        with open(HISTORICAL_FILE_NAME, "r") as fh:
            d = json.loads("[" + fh.read().replace("]", "],")[:-2] + "]")
            s3.put_object(
                Bucket="telemetry-dropoff",
                Key="historical/telemetry.json",
                Body=json.dumps(d, indent=4),
                ContentType="application/json",
                ACL="public-read",
            )
        time.sleep(SLEEP_TIME)


if __name__ == "__main__":
    main()