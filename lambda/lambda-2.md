# Lambda 2

Logging with Python Lambda.  
(so writing to cloudwatch)

## How to..

- This should be simple:  
Every write to STDIO (such as print), actually send a log to Cloudwatch Logs.  
- Just add a permission, so that your function is allowed to do so.  
(you can add a policy of permissions to the role in IAM)
- When you change your function, don't forget to deploy.