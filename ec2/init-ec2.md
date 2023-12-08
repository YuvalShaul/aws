# Initialize EC2

This is how you can run an instance, and run initialization scripts.

## Preparations

- If you don't jave a VPC yet, you can use a **default VPC**
- You should run your instance in a public subnet:
  - You should have an IGW running, attached to the VPC
  - You should be using a route table pointing to that IGW
  - In a default VPC, all subnets are public
- 
## Launch your instance

- make sure you have:
  - external ip address
  - SG that allows SSH
  - correct key-pait
- scroll to the bottom of the configuration, and open **Advanced details**
- find the **user data** pane and paste the following:  
```
#!/bin/bash
yum update -y
yum install -y git
yum install -y docker
```
- Later on, when you instance is available, you could see the user data like this:  
```
#first get the token if you don't have it yet:
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
#then get the user-data:
curl curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/user-data
```
- You may have to log out and log in again, so that the script has enough time to install.  
Then check if these tools are installed