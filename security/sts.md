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


## Get temporary credentials and using it

- A simple way to do that:  
**aws sts  get-session-token --duration-seconds 900**  
(900 seconds is the minimum)
- You'll get an access key-id, a secret access key and a token
- You can use the **aws configure** command to create a new profile:  
**aws configure --profile temp1**  
Configure the key-id and the access key.  
You shoule edit the ~/.aws/credemtials file to add the token under the new profile:  
**aws_session_token = \<token\>**
- Now you can use the new credentials, for example:  
**aws sts get-caller-identity --profile temp1**
- Try that after some time, to see that the credentials session has expired.
