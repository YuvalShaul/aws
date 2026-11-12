# List the IAM users of the account.
# Credentials come from the CLI's configuration (aws configure), never from this file:
# set AWS_PROFILE to pick a profile other than the default.
import boto3


def list_users():
    client = boto3.client('iam')
    for user in client.list_users()['Users']:
        print(user['UserName'], user['Arn'])


list_users()
