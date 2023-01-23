import boto3
import os
import json

def read_my_credentials(credfile="creds.json"):
    local_place = os.getcwd()
    cf = open( local_place + '/aws/boto3-examples/' + credfile, 'r')
    creds = json.load(cf)
    return creds

def get_all_instances_iterator():
    creds = read_my_credentials()
    ec2_resource = boto3.resource('ec2')
    instances_iterator = ec2_resource.instances.all()
    
    return instances_iterator


def demo_ec2():
    instances_iterator = get_all_instances_iterator()
    for inst in instances_iterator:
        print(inst.id, inst.state["Name"])
    print("id:", inst.id)


demo_ec2()