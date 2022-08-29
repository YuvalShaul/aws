#AWS Command Line Interface (CLI)

# Install

See instructions [here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

## Configuration

See [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-config).

# EC2

- List (and describe) AMI images:  
**aws ec2 describe-images**  
or
**aws ec2 describe-images | grep ImageId**  
(to see just the Image IDs)
- Launch an ec2 instanve:  
(example)  
**aws ec2 run-instances --image-id ami-05fa00d4c63e32376  --count 1 --instance-type t2.micro --key-name awsKP**
- List ec2 instances:  
(example)  
**aws ec2 describe-instances**  
or
**aws ec2 describe-instances |  grep InstanceId**
- Terminate instances:  
(example)  
**aws ec2 terminate-instances --instance-ids i-009ab224bfa80dda4 i-01c9d688e7ff9275d**