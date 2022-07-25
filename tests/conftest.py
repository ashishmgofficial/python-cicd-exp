import os
import pytest
from pyspark.sql import SparkSession


TEST_ROOT_DIR = os.path.dirname(os.path.realpath(__file__))


@pytest.fixture(scope="session")
def spark_session():
    session = SparkSession.builder.appName("python-testing").master("local[*]").getOrCreate()

    with session as spark:
        yield spark
