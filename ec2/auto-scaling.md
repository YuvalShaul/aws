# Auto Scaling Group


## Create a Launch Template

- Select **Launch Templates** (under **Instances**) in ec2 console page
- Click on  **Create launch template** from EC2 page
- Fill in name and description
- Check the **Auto Scaling guidance**
- specify AMI:  
Use **Quick Start**, then select **Amazon Linux aws**
- Select t2.micro as you instance type
- You don't have to choose a key pair in this walk-through
- Don't add subnets, as we will define that within the scaling group
- You may use a previous SG (if you have one) or create a new one.
- Click **Create launch template** button

## Create Scaling Group

- Choose **Auto Scaling Groups** from EC2 page, and create a new one
- Fill in a name (e.g. ASG-1)
- Choose the launch template you have already created
- click next
- Complete instance type configuration (no more than 2 vcpu..)
- Now, choose you VPC (create a defalt VPC if you don't have any)  
Add multiple subnets, so you'll have instances in different AZs.
- click next
- Select No Load Balancer
- Reduce the Helth Checks grace period to 10 seconds
- click next
- Configure 2(desired),  1(minimum), 3(maximum)  
(see the results of that later)  
- Click next (you can add SNS notification)
- Click next, you can add tags here
- click next, review and create

**MAKE SURE TO DELETE THE GROUP AND BE SURE THAT ALL INSTANCES ARE TERMINATED**
