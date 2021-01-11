import boto3

ssm = boto3.client('ssm')

def get_parameter(param_name):
    response = ssm.get_parameter(Name=param_name, WithDecryption=True)
    credentials = response['Parameter']['Value']
    return credentials
    
SECRET_KEY = get_parameter('/webchecker/JWT_SECRET_KEY')