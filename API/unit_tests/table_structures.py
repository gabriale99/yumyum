user_conf = {
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

feedback_conf = {
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

region_conf = {
    'TableName': 'region',
    'AttributeDefinitions': [
        {
            'AttributeName': 'Name',
            'AttributeType': 'S'
        }
    ],
    'KeySchema': [
        {
            'AttributeName': 'Name',
            'KeyType': 'HASH'
        }
    ],
    'ProvisionedThroughput': {
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
}

recipe_conf = {
    'TableName': 'recipe',
    'AttributeDefinitions': [
        {
            'AttributeName': 'ID',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'Region',
            'AttributeType': 'S'
        }
    ],
    'KeySchema': [
        {
            'AttributeName': 'ID',
            'KeyType': 'HASH'
        }
    ],
    'ProvisionedThroughput': {
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    },
    "GlobalSecondaryIndexes": [
        {
            'IndexName': 'Region-index',
            'KeySchema': [
                {
                    'AttributeName': 'Region',
                    'KeyType': 'HASH'
                }
            ],
            'Projection': {
                'ProjectionType': 'ALL'
            },
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        }
    ]
}

confs = [user_conf, feedback_conf, region_conf, recipe_conf]
table_names = [conf['TableName'] for conf in confs]