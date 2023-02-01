# Getting started with aws-sdk for JS

Based on [this documentation](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/getting-started-nodejs.html).

## Install nodejs on Linux

- We're downloading version 18, which is suported by AWS at this time (Jabuary 2023)
- Download the file:  
wget https://nodejs.org/dist/v18.13.0/node-v18.13.0-linux-x64.tar.gz
- Create a new directory to install it (this is what I use):  
sudo mkdir /usr/local/lib/nodejs
- Extract nodejs files into the target directory:  
sudo tar -zxf node-v18.13.0-linux-x64.tar.gz -C /usr/local/lib/nodejs/
- add the bin directory to the path:  
PATH=$PATH:/usr/local/lib/nodejs/node-v18.13.0-linux-x64/bin
