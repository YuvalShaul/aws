import json
import boto3



def create_student_table(client):
    response = client.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'StudentID',
                'AttributeType': 'N'
            }
        ],
        TableName='students',
        KeySchema=[
            {
                'AttributeName': 'StudentID',
                'KeyType': 'HASH'
            }
        ],
        BillingMode='PROVISIONED',
        ProvisionedThroughput= {
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )


def get_conf(conf_file):
    try:
        with open(conf_file, 'r') as credfile:
            confdata = json.load(credfile)
            return confdata
    except OSError :
        return {'access_key_id': None, 'secret_access_key': None, 'region': None}   


def newtab_demo():
    creds = get_conf('aws/cred.json')
    client = boto3.client('dynamodb', aws_access_key_id=creds['access-key-id'],
                                      aws_secret_access_key=creds['secret-access-key'],
                                      region_name=creds['region'])
    create_student_table(client)   

newtab_demo()