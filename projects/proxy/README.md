# Proxy to Server

This is a demo project created as part of a course.  
It demonstrates 2 servers in a row:
- a proxy server that is run as a container that runs on an EC2 docker in a public subnet
- a target server that is run in a container that runs on an EC2 docker in a private subnet.

## The Network

This is a VPC with 1 public subnet and 2 private subnets that is defined in this [vpc-proj.yaml](https://github.com/YuvalShaul/aws/blob/main/VPC/vpc-proj.yaml) cloudformation file.  
Instructions:  
- download the file to your computer (use the RAW option in github or clone the entire repository)
- Go to **cloudformation** service in the AWS console
- create a new stack, and upload the file.
- Fill in the the stack name: **my-vpc-stack**  
leave all the other default and go to next screen.
- Leave all stack options as they are, and hit **Next**
- Review all details and hit **Submit**  
Your stack and VPC are create now. This may take several minutes to complete.
- Take some time to review your VPC.  
Note the following:  
  - 3 subnets (with their names)
  - 2 routing tables (private RT attached to 2 subnets)
  - One IGW, and a default route pointing to it in the public RT
  - One NatGW, and a default route pointing to it in the private RT
  
## Security



