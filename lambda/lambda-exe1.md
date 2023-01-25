# An AWS lambda scenario with SQS

## Preparations

- (manually) - Cretae an SQS queue called **Qone**
- (manually) - Create a lambda function with permission to access this sqs queue
- (manually) - make Qone a trigger for the lambda function
- lambda code:  send message body to cloudwatch logs (so just print to standard output)
- Prepare some boto3 code to send messages to the SQS queue.  
You'll be running this code from your local environment.

## Test your scenario

When you run your local code (send some messages to the sqs queue), the following events happen:  

send from 
python code    ==>>    SQS Qone    ==>>    lambda function   ==>>   Cloudwatch logs
(local PC)
 
 You should be able to see your messages in Cloudwatch logs.