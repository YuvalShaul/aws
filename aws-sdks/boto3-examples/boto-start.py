import os
import boto3
import json


def read_my_credentials(credfile="creds.json"):
    local_place = os.getcwd()
    cf = open( local_place + '/aws/boto3-examples/' + credfile, 'r')
    creds = json.load(cf)
    return creds

def demo_boto3():
    creds = read_my_credentials()
    client = boto3.client('sts', aws_access_key_id=creds['access_key_id'],
                                      aws_secret_access_key=creds['secret_access_key'],
                                      region_name=creds['region'])
    print(client.get_caller_identity())

demo_boto3()
