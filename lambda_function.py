import os
import uuid
import json
import requests


class TodoTask:
    def __init__(self, content: str, priority: int, due_string=None, due_lang='en',
                 api_key=os.getenv('TODO_API_KEY')) -> None:
        self.content = content
        self.priority = priority
        self.due_string = due_string
        self.due_lang = due_lang
        self.api_key = api_key
        self.url = 'https://api.todoist.com/rest/v1/tasks'
        self.headers = {
            "Content-Type": "application/json",
            "X-Request-Id": str(uuid.uuid4()),
            "Authorization": f"Bearer {api_key}"
        }

    def requester(self) -> dict:
        data = json.dumps({"content": self.content,
                           "due_string": self.due_string,
                           "due_lang": self.due_lang,
                           "priority": self.priority})
        response = requests.post(
            self.url, data=data, headers=self.headers)
        return {
            "statusCode": response.status_code,
            "statusReason": response.reason,
            "data": [response.json()]
        }


def lambda_handler(event, context):
    task = TodoTask("Hello from Lambda", 4).requester()
    return task
