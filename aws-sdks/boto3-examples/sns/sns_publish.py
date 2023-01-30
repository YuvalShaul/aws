import boto3


# Get the service resource
sns_client = boto3.client('sns')
sqs_resource = boto3.resource('sns')

topic_name = 'goodreport'

response = sns_client.publish(
    TopicArn='arn:aws:sns:us-east-1:647000152682:' + topic_name,
    Message='Good reports!!!',
    Subject='rep2'
)