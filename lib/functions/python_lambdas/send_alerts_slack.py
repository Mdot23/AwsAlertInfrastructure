# 1. Get API Token from AWS Secrets Manager 
# 2. Generate API Payload function
# 3. Function to call Slac API to generate alert message
import json
import logging
import os
import boto3

""" Retrieve API token from AWS Secrets Manager"""
def get_token():
    secret_client = boto3.client('ssm')

    try:

        response = secret_client.get_secret_value(
            SecretId=SECRET_NAME
        )
    except ClientError as e:
        raise e 
    return response['SecretString']

def generate_payload(alert: dict) -> dict:
    pass

def format_message(payload: dict) -> str:
    # Slack Block Kit API includes a dedicated table block type
    pass

def send_slack_message(payload: dict):
    pass

def lambda_handler(event, context):
    pass
