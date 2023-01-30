import boto3


# Get the service resource
sns_client = boto3.client('sns')
sqs_resource = boto3.resource('sns')

topic_name = 'goodreport'
# Create a topic
response = sqs_resource.create_topic(
    Name= topic_name
)
# subscribe email
response = sns_client.subscribe(
    TopicArn='arn:aws:sns:us-east-1:647000152682:' + topic_name,
    Protocol='email',
    Endpoint='yuval.shaul@gmail.com',
)
# subscribe phone
response = sns_client.subscribe(
    TopicArn='arn:aws:sns:us-east-1:647000152682:' + topic_name,
    Protocol='sms',
    Endpoint='972503457979'
)
