"""
Purpose

Create a record DrOperations table in dynamodb.
"""

from pprint import pprint
import boto3
from datetime import datetime


def put_operation_description(operation_id, description, operation_stamp, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Operation')
    response = table.put_item(
        Item={
            'PK': operation_id,
            'SK': "description",
            'description': description,
            'operation_time': operation_stamp,
        }
    )
    return response


if __name__ == '__main__':
    operation_time = str(datetime.now())
    movie_resp = put_operation_description("20211212DrAz1ToAz2", "Dr Drill from Az1 to Az2 on 2021/12/12", operation_time)
    print("Create operation description succeeded:")
    pprint(movie_resp, sort_dicts=False)
