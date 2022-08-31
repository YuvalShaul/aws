import boto3
import json


def demo_boto3():
    client = boto3.client('iam', aws_access_key_id='AKIAVRHR5XR6NMPDRE2I',
                                      aws_secret_access_key='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',
                                      region_name='us-east-1')
    users = client.list_users()
    print(users)

demo_boto3()
