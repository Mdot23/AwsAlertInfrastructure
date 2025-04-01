import json
import logging
import os
from util import get_doc, get_description, rule
import requests
import boto3
import botocore.exceptions import ClientError 
import sys


# Logging capability 
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

CI = "CLOUD:AWS:SECURITY"
SERVICE = "url of backend service to process event"
SECRET_NAME = "/service/api-key"


def service_api_key():
    secret_client = boto3.client('ssm')

    try:

        response = secret_client.get_secret_value(
            SecretId=SECRET_NAME
        )
    except ClientError as e:
        raise e 
    return response['SecretString']

def service_post(payload: dict):
    """
    REST post request
    """
    api_key = service_api_key()


def api_payload(message: dict):
    """
    Compose payload for API by parsing non-copliant config event and extracting necessary values for the api to send 
    to service now

    returns_dict:
        environment             TEST | PROD
        configurationItem   
        severity                CRITICAL
        service                 awsConfigAlerts
        platform                AWS
        data                    JSON payload 
    """
    try:

        payload = {
            'environment': 'ITG',
            'configurationItem': CI,
            'alertName': message['configRuleName'],
            
        }
    except:
        raise 'error'
    
def lambda_handler(event, context):
    pass
