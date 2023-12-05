from datetime import datetime
import json
import os

import boto3


def lambda_handler(event, context):
    client = boto3.client("lambda")

    response = client.invoke(
        FunctionName=os.environ["api_user"], Payload=json.dumps({"uid": "uid42"})
    )
    content = json.loads(response["Payload"].read().decode())

    year = content["birthyear"]
    return {"age": datetime.now().year - year}

