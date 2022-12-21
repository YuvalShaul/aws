FROM node:19-buster
WORKDIR /awscli
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install
WORKDIR /myproj
RUN apt-get update
RUN apt-get install vim -y
RUN apt-get install nano
RUN apt-get install less
RUN npm init -y
RUN npm install aws-sdk 
CMD ["/bin/bash"]
