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

- Create a Security Group called **proxySG** that will be used to permit public access to the proxy that will run inside the public subnet.  
  - add ports 22(ssh) 
  - add 8081 (custom tcp)
- Create a Security Group called **serverSG** that will be used to permit private access from the proxy (in the public subnet) to the server running inside a private subnet.  
  - add ports 22(ssh)
  - add 9000 (custom tcp)


# Proxy EC2 Instance

- Create a new EC2 instance in the public subnet:
  - name:  proxyEC2
    - Network settings:  choose the public subnet
    - Security Group: proxySG
- Connect to the instance (ssh) and install docker:  
**ssh -i .ssh/\<pemfile.pem\>  ec2-user@\<ip address of proxy \>**
- Configure:
  - **sudo yum install docker**
  - **sudo usermod -a -G docker ec2-user**
  - **newgrp docker**
  - **sudo systemctl enable docker.service**
  - **sudo systemctl start docker.service**
- Pull the proxy image:  
**docker pull nissimo/arinetaawsproxyapp:latest**
- Run a container:  
**docker run -d -p 8081:80 nissimo/arinetaawsproxyapp:latest**  
(the proxy listens by default to port 8081)
- Browse into the proxy:  
**http://\<ip address of host\>:8081/swagger/index.html**
- You can exec into the container:  
**docker exec -it \<container name\> /bin/bash**
- You should configure the server address and port number.  
It should point to the server.  
(the file is called: appsettings,json)
- Restart the containers:  
**docker restart \<container name\>

# Server EC2 Instance

  - name serverEC2
    - Network settings: choose priv1-subnet
    - Security Group: serverSG

  - Login into proxyEC2 and from there into serverEC2:
    - copy your private key into the the proxy (see example):  
    **scp -i .ssh/yuvKP.pem /home/yuval/.ssh/yuvKP.pem   ec2-user@52.0.144.95:/home/ec2-user/.ssh**
    - ssh into the proxy
    - ssh into the server using the private IP address
  - Install docker:  
  - **sudo yum install docker**
  - **sudo usermod -a -G docker ec2-user**
  - **newgrp docker**
  - **sudo systemctl enable docker.service**
  - **sudo systemctl start docker.service**
  - Pull the proxy image:  
**docker pull nissimo/arinetaawsapp:latest**
  - Run a container:  
  **docker run -d -p 9000:80 nissimo/arinetaawsapp:latest**

# Try out the API

Use the following to try the app:  
**http://\<proxy IP address \>/swagger/index.html**

