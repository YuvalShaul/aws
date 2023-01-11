# ECS Fargate - Getting Started

A simple way to create a (very simple) complete application with ECS

## Using the Get Started option

- Choose the ECS (Ellastic Container Service) and get the [main page](https://us-east-1.console.aws.amazon.com/ecs/home?region=us-east-1).
- Choose **Clusters** from the left pane.  
(there are no clusters yet)
- Click on the **Get Started** button.  
You should see this image:  
![Diagram of ECS objects and how they relate](https://d37snh6s3haxnv.cloudfront.net/ecs-objects-taskdef-1aba4ac72a5c999e0cb74833a18e6289eb71d32a.png)

## Container and Task definition

- We'll be using a single container image for our app.
- Select **nginx** options (make sure it is blue)
- The name you choose is passed directly to docker daemon, so in this case the image is going to be downloaded from the [dockerhub](https://hub.docker.com/)  
(see [here](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#container_definition_image) for more details)
- Click on the **edit** button to see what other container setting you can set (but don't change anything)
- Go over the **task definition** details (you can also click on the **edit** button)
- When you're done, click **next** at the bottom

## Service definition

- In this phase, you can choose the amount of tasks to create based on your task definition  
Choose **2** to run 2 tasks in a single service (and **save**)
- There's also a security group definition here (just read the details)
- We'll not be using a load-balancer in this walkthrough
- Click **next**

## Cluster definition

- We'll change nothing here, since this is a Fargate cluster.
- A new VPC and subnets will be created for us
- Click **next**
- There is a review page where you can edit all details
- Click **Create** !!!

## Testing your app

- It may take several **minutes** until your app is ready
- The IP addresses to use will be inside the tasks, so each task will be working independently.
- Look for the external IP address in each task, and browse it
- Don't forget to delete your tasks, because these are **tasks** you are paying for.