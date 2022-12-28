# Build Your VPC

A VPC exercise, to create your entire VPC, that invludes:
- 4 subnets (2 public, 2 private)
- 2 routing tables (public and private)
- an Internet Gateway (IGW)
- a NAT Gateway (NGW)
- security groups
- instances in public subnets (accessible from the Internet)
- instances in private subnets (accessible from private subnets)

## Create the VPC

- fast pace:  
Create a VPC called **vpcA**, with IPv4 CIDR:  10.0.0.0/16 (no IPv6)

Detailed:  
- Find the VPC service inside the AWS Console.
- Click on **Create VPC**
- Choose **VPC only**, as you are learning and want to create everything from scratch.
- Give your VPC a name: **vpcA**  (don't change this name, as I'll refer to it later, and also in other walk-through documents)
- An IPv4 CIDR block for the VPC:  
Use 10.0.0.0/16 (not what the AWS console suggests)  
No IPv6 CIDR block for this session
- Leave **Tenancy** as Default
- Scroll to the bottom of the page and hit **Create VPC**

## Create Subents

- Create 4 subnets.
- Note that each subnet resides within ONE AZ  
(but multiple subnets may reside within a single AZ)
- Details:
  - pubA1  (10.0.0.0/24)  (vpcA, public subnet 1) in us-east-1a
  - privA1 (10.0.1.0/24)  (vpcA, private subnet 1)  in us-east-1a
  - pubA2  (10.0.2.0/24)  (vpcA, public subnet 2)  in us-east-1b
  - privA2 (10.0.3.0/24)  (vpcA, private subnet 1)  in us-east-1b

## Create Routing Tables

There is already a single routing table.  
Name it **main-vpcA** (you can do that from the main listing of route tables)  
You will not be using this routing table.  

Create 2 new routing tables:
- pubA-RT
- privA-RT
(the **A** here reserves these route tables for vpcA)

Now attach those to the correct subnets:  

- privA-RT to privA1 and privA2
- pubA-RT  to pubA1  and pubA2

## Fix Public Routing Tables

Add default routes to public routing tables:
- Create a new internet gateway called **vpcA-IGW**
- Attach the IGW to vpcA
- Add a defult route to this IGW:
  - only in the single public route table
  - 0.0.0.0/0  pointing to the IGW
**note: this is what make the subnets associated with this RT public!**

## Create an Instace in a public subnet

We can connect to this one using SSH from the global Internet.  

- Name:  **pubA1-EC2**
- Details: AMI2, t2-micro
- Edit networking: choose subnet pubA1
- External IP address: enabled
- key-pair: either create a new one, or use an existing one
- Security group:  Create a new one called **ssh-only**, that allows only SSH protocol (TCP port 22)  

Launch your instance and make sure you can connect to it: 
exalple (change to your key-pair value and correct external IP address):   
**ssh -i ~/.ssh/awsKP.pem ec2-user@52.7.123.220**


You should be able to login into the instance

##  An instance in a private subnet

- Create an instance in subnet **privA1** called **privA1-EC2**
  - NO EXTERNAL IP ADDRESS
  - Same key-pair, security group
  - make sure you edit the networking and put it on the correct subnet (privA1)
  - You could connect to this one from the public instance:
    - copy your key-pair from your host to pubA1-EC2:  
    Example (change IP address and name of key-pair file):  
    **scp -i ~/.ssh/awsKP.pem  ~/.ssh/awsKP.pem ec2-user@52.7.123.220:/home/ec2-user/.ssh**
    - connect to pubA1-EC2 and from there to privA1-EC2 (using the private IP address).  
    Example:  
    **ssh -i ~/.ssh/awsKP.pem  ec2-user@10.0.1.91**

## Nat Gateway

Your new, private instance is not connected to the internet at all.  
We can connect it in a way that'l allow it to download software and updates.  
It will still not be able to directly connect to it fron the global Internet.  
We'll use a NAT Gateway for that.

- Create a new Nat Gateway called **vpcA-NGW**
- Make sure you put it in a **public subnet**, it our case:  **pubA1**
- Allocate a new ellastic IP address for it
- It may take some time until it is available to use (it goes to Available state)
- To use it, add a default route poing to it in the **private route table (privA-RT)
- After doing that, try to see if the private instance can update some software:  
  - **sudo yum update**
  - **sudo yum install httpd**  
  (not that this is going to be usefull)


Hope you enjoyed this one!

