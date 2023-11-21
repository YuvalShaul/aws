# Identity based policy - EC2

In this lab we are going to create an IAM Identity based policy.  
Read more about [the difference between identity-based and resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html). There are [some examples for Idenetity-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_examples.html)  
Remember that an identity-based policy describes what can be done with a resource, and we'll later attach this one to a user, group or role.

## Create an EC2 instance

Use your aws user to create an ec2 instance:
- you don't need any external ip address
- you don't need a keypair
- choose t2.micro (for free tier compliance)



## New IAM user

- Create a new iam user (I have chosen the name dave)
- do not add any permissions for your new user
- make sure you get your console credentials
- open a new browser to login to the aws console with the new user  
(for example - use chrome if you were using firefox)  
This way you can login into aws with these 2 accounts at once.
- Try to see the list of the current ec2 instances (you are not able to do so)


## Add a policy to your user

- In your main user go to IAM and create a new policy
- Select ec2 as the service
- Add **DescribeInstances** to the list of allowed actions
- Allow all instances (so use **\*** of choose **All**)
- If you seitch to json, you should see something like this:

```
{
  "Version": "2012-10-17",
  "Statement": [
      {
          "Effect": "Allow",
          "Action": "ec2:DescribeInstances",
          "Resource": "*"
      }
  ]
}
```

- Hit **Next** and choose a name for your policy (maybe **see-ec2** ??)
- Attach the policy to user **dave**.  
You can do this from the policy (or policies), and also from the user.
- Try to look at the running instances again
- good luck!