
from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext


def lambda_handler(event: dict, context: LambdaContext):
    print(f"Enter to function handler: event: {event}")


    return {
        'statusCode': 200
    }