# Create an IAM user.
# Credentials come from the CLI's configuration (aws configure), never from this file:
# set AWS_PROFILE to pick a profile other than the default.
import boto3


def add_user(user_name):
    client = boto3.client('iam')
    response = client.create_user(UserName=user_name)
    print(response['User']['Arn'])


add_user('new-user')
