# Tutorial: Create a Classic Load Balancer

We'll follow the tutorial from [this link](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-getting-started.html)

## Details
- Choose a region
- Your VPC:
  - 1 private subnets in different AZ
  - 2 public subnet in the same AZ as the private subnets
  - public route table with a route to an IGW
  - private route table
  - Create a single security group that opens HTTP to hosts from the VPC, and SSH to anybody.
  - Make sure your private subnets CAN reach the public internet, because you'll have to install a web server on your private servers.
- Your hosts:
  - One on each private subnet (you'll install a web server on those) 
  - One in the public network to connect to the private ones.


## To help you

- Here's an example of copying your keypair to aws:  
**scp -i yuvKP.pem yuvKP.pem   ec2-user@18.212.23.236:/home/ec2-user/.ssh
yuvKP.pem**
- Installing a web server:  
```
sudo yum update -y
sudo yum install -y httpd.x86_64
sudo systemctl start httpd.service
sudo systemctl enable httpd.service
```

