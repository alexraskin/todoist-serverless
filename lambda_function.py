import os
import uuid
import json
import requests

# set inside lambda
api_key = os.getenv('TODOIST_API_KEY')


def lambda_handler(event, context):
    headers = {
        "Content-Type": "application/json",
        "X-Request-Id": str(uuid.uuid4()),
        "Authorization": f"Bearer {api_key}"
    }
    data = json.dumps({"content": "This task was created using AWS Lambda",
                                              "due_string": "today at 8am",
                                              "due_lang": "en",
                                              "priority": 4})
    response = requests.post('https://api.todoist.com/rest/v1/tasks',
                             data=data,
                             headers=headers)
    if response.status_code == 200:
        return {
            "statusCode": response.status_code
        }
    else:
        return {
            "statusCode": response.status_code
        }
