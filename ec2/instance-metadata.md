# EC2 user Data

We used the IMDSv2 as described [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html).

## Create an instance

- Create a simple ec2 instance and include some user-data in it

## Get the toekn

- Use [**curl**](https://en.wikipedia.org/wiki/CURL) to get the session token.
```
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
```
  - the -X option means that we specify the HTTP command to use (PUT in this case)
  - the -H specified an HTTP header, which confirm that this is going to be IMDSv2 and not IMDSv1, and also specify the session time

- The use the token with **curl** to get [instance data categories](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-categories.html):
```
curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/
```

## Get some data

- get the hostname (compare to the **hostname** command)
- get the instance id (see also in the console)
- mac address of the local interface
- Public IPv4 address

## Get user data

- Get your user data:
```
curl curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/user-data
```