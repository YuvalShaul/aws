# boto3

The famous aws python sdk library.

## Documentation

- Go to the [latest docs](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html).
- Go to [the pip installation page](https://pypi.org/project/boto3/).

##  Installaion

- Create a new virtual environment:  
(to be compatible with this git repository, use **venv** as a name)  
**python3 -m venv \<virtual env name\>**
- Activate the virtual environment:  
**source \<virtual env name\>/bin/activate**
- Install:  
**pip install boto3**

## Creating a json credentials file

- Use **cred.json** to be compatible with this repository
- Here's an example:
```
{
    "access_key_id": ".....",
    "secret_access_key": "....", 
    "region": "us-east-1"
}
```
