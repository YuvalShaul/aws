# Lab: Getting Started with AWS

This lab is the hands-on part of the lesson [Getting Started with AWS](https://www.yuval.guide/aws/01-cloud-and-account/aws-getting-started/)
on yuval.guide: each step links the slide that shows how to do it.

- The lab opens an AWS account and protects it with MFA and a budget.
- It ends with the group `developers` holding two users: `alice`, created in the console, and `bob`, created from the CLI.

## Read about the account and its costs

1. Read the slides [The AWS account](https://www.yuval.guide/aws/01-cloud-and-account/aws-getting-started/?s=account),
   [AWS pricing](https://www.yuval.guide/aws/01-cloud-and-account/aws-getting-started/?s=pricing) and
   [The credit card and the course's costs](https://www.yuval.guide/aws/01-cloud-and-account/aws-getting-started/?s=cost).

## Get an AWS account

<details>
<summary>Option 1: you have no AWS account</summary>

1. Follow [Sign up for an AWS account](https://www.yuval.guide/aws/01-cloud-and-account/aws-getting-started/?s=open-account).
2. Wait for AWS's email saying the account is active.

</details>

<details>
<summary>Option 2: you already have an AWS account</summary>

1. Find the account's root email address and password.
   - The course signs in as the root user in this session.

</details>

## Sign in as the root user

1. Follow [Sign in as the root user](https://www.yuval.guide/aws/01-cloud-and-account/aws-getting-started/?s=sign-in).
2. Check that the page is headed **Console Home**.

## Turn on MFA for the root user

1. Pick a device: [The three kinds of MFA device](https://www.yuval.guide/aws/01-cloud-and-account/aws-getting-started/?s=mfa-devices).
2. Follow [Turn on MFA for the root user](https://www.yuval.guide/aws/01-cloud-and-account/aws-getting-started/?s=mfa).
3. Sign out, and sign in again as the root user.
   - Check that the sign-in asks for your MFA device after the password.

## Set a zero-spend budget

1. Follow [Set a zero-spend budget](https://www.yuval.guide/aws/01-cloud-and-account/aws-getting-started/?s=budget).
2. Check that **Budgets** lists the new budget.

## Create the group and the user in the console

1. Follow [Create the group developers](https://www.yuval.guide/aws/01-cloud-and-account/aws-getting-started/?s=create-group).
2. Follow [Create the user alice](https://www.yuval.guide/aws/01-cloud-and-account/aws-getting-started/?s=create-user).
3. Check them as [Display the users and groups](https://www.yuval.guide/aws/01-cloud-and-account/aws-getting-started/?s=show-users) shows:
   - **Users** lists `alice`, in the group `developers`.
   - The group `developers` lists `alice` under **Users**.

## Open CloudShell

1. Follow [Open CloudShell](https://www.yuval.guide/aws/01-cloud-and-account/aws-getting-started/?s=cloudshell).
2. Check that `aws iam list-users` lists `alice`.

## Set up the CLI on your computer

1. Follow [Install the AWS CLI on your computer](https://www.yuval.guide/aws/01-cloud-and-account/aws-getting-started/?s=install-cli).
2. Follow [Sign the CLI in with aws login](https://www.yuval.guide/aws/01-cloud-and-account/aws-getting-started/?s=aws-login).
3. Check that `aws sts get-caller-identity` names your account's root user.

<details>
<summary>No computer of your own to install on?</summary>

1. Run the rest of the lab in CloudShell: its CLI is already signed in.

</details>

## Read the users and groups from the CLI

1. Follow [Read the users and groups from the CLI](https://www.yuval.guide/aws/01-cloud-and-account/aws-getting-started/?s=cli-read).
2. Check that `get-group` lists `alice` in `developers`.

## Create the user bob from the CLI

1. Follow [Create the user bob from the CLI](https://www.yuval.guide/aws/01-cloud-and-account/aws-getting-started/?s=cli-create).
2. Check the result in both tools:
   - `aws iam get-group --group-name developers --query 'Users[].UserName'` lists `alice` and `bob`.
   - In the console, the group `developers` lists both under **Users**.
