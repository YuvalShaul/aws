# Resource Based Policy

Resource based policies are eventually attached to a **resource**, hence have an added element in their policy document.
Since they are attached to a resource, they should specify the identity(es) that the policy refers to, so it has a [**Principal** element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-accounts) in its definition.  
Very few resources support resource based policies (see [this list](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) for more details)
