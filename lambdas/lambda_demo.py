import json
import logging


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
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully test lambda')
    }

