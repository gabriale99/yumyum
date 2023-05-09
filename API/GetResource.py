import boto3
import simplejson as json

def lambda_handler(event, context):
    client = boto3.resource('dynamodb')
    table_name = event['queryStringParameters']['table']
    table = client.Table(table_name)
    output = []
    
    # Set the pagination parameters
    page_size = 100  # The maximum number of items to retrieve per page
    
    # Initialize the starting key to None
    last_evaluated_key = None
    # Loop through all pages of results
    while True:
        # Build the query parameters
        query_params = {
            'Limit': page_size
        }
    
        # Add the ExclusiveStartKey to the query parameters if it's not None
        if last_evaluated_key:
            query_params['ExclusiveStartKey'] = last_evaluated_key
    
        # Query the table and retrieve the page of results
        response = table.scan(**query_params)

        for item in response['Items']:
            output.append(item)

        # Check if there are more pages to retrieve
        last_evaluated_key = response.get('LastEvaluatedKey')
        if not last_evaluated_key:
            break
    
    output = [o['Name'] for o in output]
    
    return {
       'statusCode': 200,
       'headers': {
            'Content-Type': 'application/json',
            "Access-Control-Allow-Origin" : "*", # Required for CORS support to work
            "Access-Control-Allow-Headers" : "Content-Type",
        },
       'body': json.dumps({
           "output": output
       })
    }


response = lambda_handler({
            "queryStringParameters": {
                "table": "ingredient"
            }
        }, None)
print(response)