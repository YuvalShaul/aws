import boto3
import json


def add_my_user(user_name):
    client = boto3.client('iam', aws_access_key_id='AKIAVRHR5XR6NMPDRE2I',
                                      aws_secret_access_key='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',
                                      region_name='us-east-1')
    response = client.create_user(UserName = user_name)
    print(response)


add_my_user('new-user')
