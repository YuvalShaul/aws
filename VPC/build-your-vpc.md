# Build Your VPC

A VPC exercise, to create your entire VPC, that invludes:
- 4 subnets (2 public, 2 private)
- 4 routing tables
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

- Create 4 subnets:
  - pubA1  (10.0.0.0/24)  (vpcA, public subnet 1)
  - privA1 (10.0.1.0/24)  (vpcA, private subnet 1)
  - pubA2  (10.0.2.0/24)  (vpcA, public subnet 2)
  - privA2 (10.0.3.0/24)  (vpcA, private subnet 1)

## Create Routing Tables

There is already a single routing table.  
Name it **main-vpcA** (you can do that from the main listing of VPCs)  
You will not be using this routing table.  

Create 4 new routing tables:
- pubA1-RT
- privA1-RT
- pubA2-RT
- privA2-RT

Now attach those to the correct subnets:
- pubA1-RT  to pubA1
- privA1-RT to privA1
- pubA2-RT  to pubA2
- privA2-RT to privA2

## Fix Public Routing Tables

Add default routes to public routing tables:
- 