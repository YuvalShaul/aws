# AWS Javascript Docker Image

## Features of this image

The Dockerfile from this directory can be used to create an image with the following features:
- Based on Debian (buster is Debian 10)
- It has a nodejs installation (version v19.2.0)
- Has aws JS sdk installed (in a directory called **/myproj**)
- Has aws-cli installed (version 2.9.6)
- Some other tools: vim, nano, less


## Build the Image

Here's an example of the build command:  
**docker build . -t aws-node:19**  

This will build an image called aws-node:19

## Using the image

- Run an interractive container from this image:  
(container is called **aws1** in this example)    
**docker run -it --name=aws1 aws-node:19**
- The default command is **/bin/bash**, so you'll get a running shell.
- You can exec into the container (to run node) from another window:  
**docker exec -it aws1 node**
