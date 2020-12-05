import boto3

# Get the service resource
sqs = boto3.resource('sqs')

print('*** access a single queue ***')

# Get the queue. This returns an SQS.Queue instance
queue = sqs.get_queue_by_name(QueueName='henryqueue')

# You can now access identifiers and attributes
print(queue.url)
print(queue.attributes.get('DelaySeconds'))

print('*** access all queues ***')

# Print out each queue name, which is part of its ARN
for queue in sqs.queues.all():
    print(queue.url)