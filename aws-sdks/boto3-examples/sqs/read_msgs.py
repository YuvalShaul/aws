import boto3
import json


# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='Q1')
msgs = queue.receive_messages(MaxNumberOfMessages =5, WaitTimeSeconds=10)
for msg in msgs:
    print(msg.body)
    msg.delete()
pass
