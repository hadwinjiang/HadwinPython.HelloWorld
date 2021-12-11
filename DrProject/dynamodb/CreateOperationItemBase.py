"""
Purpose

Create a record DrOperations table in dynamodb.
"""

from pprint import pprint
import boto3
from datetime import datetime


def put_operation(operation_id, instance_id, operation_stamp, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Operation')
    response = table.put_item(
        Item={
            'PK': operation_id,
            'SK': instance_id,
            'operation_time': operation_stamp,
        }
    )
    return response


if __name__ == '__main__':
    operation_time = str(datetime.now())
    movie_resp = put_operation("20211212DrAz1ToAz2", "i-0911c5f0d337036fd", operation_time)
    print("Put movie succeeded:")
    pprint(movie_resp, sort_dicts=False)
