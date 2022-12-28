# VPC Peering exercise

In this walkthrough we'll create a peering between 2 VPCs, in different regions.  
One of the VPCs is the one we have created in [Build Your VPC](https://github.com/YuvalShaul/aws/blob/main/VPC/build-your-vpc.md) exercise.  


## Create a new VPC 

- **Make sure that you are now in us-east-2 (Ohio) region**
- create a new vpc called vpcB
- use 10.1.0.0/16 as a CIDR for the VPC

## Subnets and routing tables

- create 2 subnets:
  - pubB (10.1.0.0/24) with route table pubB-RT (AZ: us-east-2a)
  - privB (10.1.1.0/24) with route table privB-RT (AZ: us-east-2b)

## Instances

- go into EC2 configuration page
- make sure that you are still in Ohio (us-east-2) region
- launch **pubB-EC2** in subnet pubB, with external IP address
- launch **privB-EC2** in subnet privB, with NO external IP address
- To enable **ping** test:
  - edit attached security groups to allow all ICMP IPv4 from all addresses
  - repeat this in the instances of us-east-1

## VPC Peering

- vpcA requester - vpcB
- make sure you are in N.Virginia, go to VPC and select **Peering connections**
- Create a new peering, and fill the details:
  - local - vpcA
  - remote region (find Ohio)
  - remote VPC ID (find in another tab)
  - create
- You can see that your peering connection is in the pending state
- Go to Ohio, select peerings there and accept the connection.  
It is now in **Actibe** state

## Update Routing tables to point to the peering

- Routing tables:
  - add a route to 10.1.0.0/16 pointing to the peering connection in both vpcA route tables
  - add a route to 10.0.0.0/16 pointing to the peering connection in both vpcB route tables

## Test

You should be able to ping from all ec2 instances to all instances.

