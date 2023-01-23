import boto3
import os
import json

def read_my_credentials(credfile="creds.json"):
    local_place = os.getcwd()
    cf = open( local_place + '/aws/boto3-examples/' + credfile, 'r')
    creds = json.load(cf)
    return creds

def create_instance():
    creds = read_my_credentials()
    ec2_resource = boto3.resource('ec2', aws_access_key_id=creds['access_key_id'],
                                      aws_secret_access_key=creds['secret_access_key'],
                                      region_name=creds['region'])
    instances = ec2_resource.create_instances(
        ImageId="ami-0b5eea76982371e91",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="yuvKP")
    return instances


def demo_ec2():
    instances = create_instance()
    inst = instances[0]
    print("id:", inst.id)
    print()


demo_ec2()