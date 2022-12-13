# AWS Javascript Image

## Features of this image

The Dockerfile from this directory can be used to create an image with the following features:
- Based on Debian (buster is Debian 10)
- nodejs installation (version v19.2.0)
- Has aws JS sdk installed 
- Has aws-cli installed (version 2.9.6)

## Build the Image

Here's an example of the build command:  
**docker build . -t aws-node:19**  

This will build an image called aws-node:19

## Using the image

- Run an interractive container from this image:  
(container is called **aws1** in this example)    
**docker run -it --name=aws1 aws-node:19**
- Exec into the container (running bash) so that you can run aws cli commands:  
**docker exec -it aws1 /bin/bash**
- There's vim installed if you need a text editor inside the container.
