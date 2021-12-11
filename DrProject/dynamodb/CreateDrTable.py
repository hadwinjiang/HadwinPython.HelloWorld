"""
Purpose

Shows how to create an Amazon DynamoDB table for storing Operations.
operation_id is used as a primary partition key 
instance_id as a secondary sort key.
"""

import boto3


def create_operation_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.create_table(
        TableName='Operation',
        KeySchema=[
            {
                'AttributeName': 'PK',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'SK',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'PK',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'SK',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        },
        Tags=[
            {
                "Key": "auto-delete",
                "Value": "no"
            }
        ]
    )
    return table


if __name__ == '__main__':
    movie_table = create_operation_table()
    print("Table status:", movie_table.table_status)
