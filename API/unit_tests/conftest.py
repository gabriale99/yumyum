import boto3
import pytest
from .table_structures import *

@pytest.fixture(scope='class', autouse=True)
def create_tables():
    db_client = boto3.client('dynamodb', endpoint_url='http://localhost:8000')


    db_client.create_table(**user_table)
    db_client.create_table(**feedback_table)

    yield

    db_client.delete_table(TableName='user')
    db_client.delete_table(TableName='feedback')