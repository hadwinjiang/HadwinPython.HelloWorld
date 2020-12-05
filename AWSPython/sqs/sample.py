import boto3

client = boto3.client('sqs')

response = client.list_queues(
    QueueNamePrefix='henry',
    # NextToken='string',
    MaxResults=123
)

print(response)