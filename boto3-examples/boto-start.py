import os
import boto3
import json


def read_my_credentials(credfile="cred.json"):
    cf = open(os.getcwd() + '/aws/' + credfile, 'r')
    creds = json.load(cf)
    return creds

def demo_boto3():
    creds = read_my_credentials()
    client = boto3.client('sts', aws_access_key_id=creds['access-key-id'],
                                      aws_secret_access_key=creds['secret-access-key'],
                                      region_name=creds['region'])
    print(client.get_caller_identity())

demo_boto3()
