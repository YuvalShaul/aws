# Role Lab

In this lab we are going to do the following:
- create a user with full ec2 permissions
- create a role with a trust policy that enables that user
- try to assume role from a different user (and fail)
- now assume and check that new priviledges are there

## Create a user

- Create a new user (let's call her Clara)
- Add the **AmazonEC2FullAccess** AWS managed policy
- convince yourself that clara can create and terminate ec2 instances, but nothing else

## Create a role

- Create a role called **ec2-closer**, such that:
  - only Clara can assume this role (so use **Custom trust policy**)
  - Create your own policy for the role called **ec2-closer-policy** with these 3 allowed operations:
    - StopInstances
    - TerminateInstances
    - DescribeInstances
  - Add this policy to the role


## Assume the role

- log into Clara's account
- make sure you have an ec2 instance (created from Claras account)
- Assume the role
- see if you can create another instance
- make sure you can stop and terminate the first instance.

