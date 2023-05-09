#!/bin/bash

# Check if the dynamodb_local_latest folder exists
if [ ! -d "dynamodb_local_latest" ]; then
    echo Folder does exists
    echo Installing the folder now
    curl -L https://s3.us-west-2.amazonaws.com/dynamodb-local/dynamodb_local_latest.zip > dynamodb_local_latest.zip
    unzip dynamodb_local_latest.zip -d dynamodb_local_latest/
    rm dynamodb_local_latest.zip
fi

echo "Going to dynamodb_local_latest"
cd dynamodb_local_latest
echo "Starting DynamoDB Local..."
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb &
echo "DynamoDB Local started."

cd ..
cd API/unit_tests
echo "Running pytest"
python -m coverage run -m pytest
python -m coverage report
python -m coverage html

read -rsp $'Press any key to stop DynamoDB Local...\n' -n1
echo "Stopping DynamoDB Local..."
kill $!
echo "DynamoDB Local stopped."
