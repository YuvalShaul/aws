import json
import boto3



def insert_into_people(client, first_name, phone_number):
    new_item={
        'name': {
            'S': first_name,
        },
        'phone': {
            'S': phone_number
        }
    }
    
    response = client.put_item(
        TableName='people',
        Item = new_item,
        ReturnConsumedCapacity='TOTAL'
    )

def get_conf(conf_file):
    try:
        with open(conf_file, 'r') as credfile:
            confdata = json.load(credfile)
            return confdata
    except OSError :
        return {'access_key_id': None, 'secret_access_key': None, 'region': None}   


def dynamodb_demo():
    creds = get_conf('aws/cred.json')
    print(creds)
    client = boto3.client('dynamodb', aws_access_key_id=creds['access-key-id'],
                                      aws_secret_access_key=creds['secret-access-key'],
                                      region_name=creds['region'])
    insert_into_people(client, 'Dave', "09-1234567")
    insert_into_people(client, 'Aisha', "09-9876543", details={'address':{'S':'New-York'}, 'role':{'S':'student'}})
    

dynamodb_demo()