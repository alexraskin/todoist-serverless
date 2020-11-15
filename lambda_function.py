import requests
import uuid
import json

api_key = '<api-key>'

def lambda_handler(event, context):
    reponse = requests.post("https://api.todoist.com/rest/v1/tasks", 
                    data = json.dumps({ "content": "This task was created using AWS Lambda",
                        "due_string": "today at 8am",
                        "due_lang": "en",
                        "priority": 4}),
                    headers={
                        "Content-Type": "application/json",
                        "X-Request-Id": str(uuid.uuid4()),
                        "Authorization": "Bearer %s" % api_key
                    })
    print reponse
    print reponse.text