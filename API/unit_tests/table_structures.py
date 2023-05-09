user_table = {
    'TableName': 'user',
    'AttributeDefinitions': [
        {
            'AttributeName': 'UserID',
            'AttributeType': 'S'
        }
    ],
    'KeySchema': [
        {
            'AttributeName': 'UserID',
            'KeyType': 'HASH'
        }
    ],
    'ProvisionedThroughput': {
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
}

feedback_table = {
    'TableName': 'feedback',
    'AttributeDefinitions': [
        {
            'AttributeName': 'UserID',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'FeedbackDateTime',
            'AttributeType': 'S'
        },
    ],
    'KeySchema': [
        {
            'AttributeName': 'UserID',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'FeedbackDateTime',
            'KeyType': 'RANGE'
        }
    ],
    'ProvisionedThroughput': {
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
}