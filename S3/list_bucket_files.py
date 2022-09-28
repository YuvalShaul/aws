import json
import boto3


def get_conf(conf_file):
    try:
        with open(conf_file, 'r') as credfile:
            confdata = json.load(credfile)
            return confdata
    except OSError :
        return {'access_key_id': None, 'secret_access_key': None, 'region': None}   

def list_S3_files(bucket_name):
    creds = get_conf('aws/cred.json')
    s3_client = boto3.client('s3', aws_access_key_id=creds['access-key-id'],
                                      aws_secret_access_key=creds['secret-access-key'],
                                      region_name=creds['region'])
    response = s3_client.list_objects(Bucket=bucket_name)
    if 'Contents' in response:
        files = [item['Key'] for item in response['Contents']]
        print(files)


list_S3_files('mybucket1247615347')