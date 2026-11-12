# AWS CLI: Installation and Configuration

## Install

- Follow the [installation instructions](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) for your system.
- Check it:  
**aws --version**

## Prerequisites

- You should have:
  - An IAM account
  - an **access key id** for that account
  - a matching **secret access key**
  - more details [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)

## Try it

- Type:  
**aws configure**
- Follow the instructions.  
(you should choose a regions like us-east-1, and a preffered output format: json/yaml)
- Edit ~/.aws/credentials to see the results  
(in the case of a docker container, ~ is going to be /root directory)