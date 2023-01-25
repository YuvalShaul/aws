import boto3
import os
import json


def get_all_instances_iterator():
    ec2_resource = boto3.resource('ec2')
    instances_iterator = ec2_resource.instances.all()
    
    return instances_iterator


def demo_ec2():
    instances_iterator = get_all_instances_iterator()
    for inst in instances_iterator:
        print(inst.id, inst.state["Name"])

demo_ec2()