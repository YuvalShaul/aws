# STS - Secure Token Service

## Links

- [STS Python boto3 docs](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html).
- [STS Javascript SDK docs](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/STS.html)
- [STS cli](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/index.html)

## cli smaples

- Who is using aws?  
**aws sts get-caller-identity**
- What is the account of this access key id?  
**aws sts get-access-key-info --access-key-id \<value\>**
- Assuming a role (and getting credentials and security token):  
**aws sts assume-role --role-arn arn:aws:iam::647000152682:role/S3-master  --role-session-name s3-work**