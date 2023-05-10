import boto3
import logging
import pytest
from .table_structures import confs, table_names
from .populate_db import populate_data

logging.basicConfig(filename="unit_test.log")

@pytest.fixture(scope='class', autouse=True)
def create_tables():
    db_client = boto3.client('dynamodb', endpoint_url='http://localhost:8000')

    for conf in confs:
        try:
            db_client.create_table(**conf)
        except Exception as e:  #  pragma: no cover
            logging.error(e)
            continue

    populate_data()

    yield


    for name in table_names:
        try:
            db_client.delete_table(TableName=name)
        except:  #  pragma: no cover
            continue