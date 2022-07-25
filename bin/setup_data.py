import os
import logging
import boto3
from botocore.client import Config
import botocore
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_s3.service_resource import S3ServiceResource
else:
    S3ServiceResource = object

from dotenv import load_dotenv

logging.basicConfig(
    level="INFO",
    format="%(asctime)s — %(levelname)s — %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)


def upload_datadir_to_s3(s3: S3ServiceResource, path: str, bucketname: str):
    bucket = s3.Bucket(name=bucketname)
    for root, dirs, files in os.walk(path):
        for file in files:
            bucket.upload_file(os.path.join(root, file), file)
    return True


def check_bucket_exists(s3: S3ServiceResource, bucketname: str) -> bool:
    # bucket = s3.Bucket(name=bucketname)
    exists = True
    try:
        s3.meta.client.head_bucket(Bucket=bucketname)
    except botocore.exceptions.ClientError as e:
        # If a client error is thrown, then check that it was a 404 error.
        # If it was a 404 error, then the bucket does not exist.
        error_code = e.response["Error"]["Code"]
        if error_code == "404":
            exists = False
    return exists


def main():
    s3 = boto3.resource(
        "s3",
        endpoint_url="http://localhost:9000",
        config=Config(signature_version="s3v4"),
        region_name="us-east-1",
    )
    buckets = ["staging", "processed", "consumption"]
    for bucket in buckets:
        if not check_bucket_exists(s3, bucketname=bucket):
            s3.create_bucket(Bucket=bucket)

    upload_datadir_to_s3(s3, path="input", bucketname="staging")


if __name__ == "__main__":
    logging.info("Looking for environment variables required..")
    load_dotenv()

    main()
