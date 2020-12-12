import json
import logging
import os

import boto3 as boto3

stepfunctions = boto3.client('stepfunctions')
state_machine_arn = os.environ['STEP_FUNCTION_ARN']


def configure_logging():
    root = logging.getLogger()
    if root.handlers:
        for handler in root.handlers:
            root.removeHandler(handler)

    logging.basicConfig(format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
                              datefmt='%m-%d %H:%M:%S', level=logging.INFO)


def lambda_handler(event, context):
    # check default lambda_logger.py handlers to enable info lambda_logger.py
    configure_logging()
    logging.info("testing lambda info logging")
    step_functions_response = stepfunctions.start_execution(
        stateMachineArn=state_machine_arn,
        input=json.dumps({'data': event})
    )
    logging.info(f"step function response: {step_functions_response}")
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully test step functions lambda')
    }

