import os
import sys
import openai
import json
from typing import TypedDict

from aws_lambda_typing import context as context_, events

class GPTMessage(TypedDict):
    role: str
    content: str

class EventBodyRequired(TypedDict):
    message: str

class EventBody(EventBodyRequired, total=False):
    messageHistory: list[GPTMessage]

def handler(event: events.APIGatewayProxyEventV2, context: context_.Context):
    body: EventBody = json.loads(event["body"])

    initial_system_message = os.getenv("INITIAL_SYSTEM_MESSAGE")
    print("INITIAL_SYSTEM_MESSAGE: ", initial_system_message)

    messages: list[GPTMessage] = []

    if initial_system_message:
        messages = [{"role": "system", "content": initial_system_message}]

    if "messageHistory" in body:
        messages.extend(body["messageHistory"])

    messages.append({"role": "user", "content": body["message"]})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    message = response["choices"][0]["message"]["content"]
    return message

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: python app.py <input>")
        sys.exit(1)
    print(handler({ "body": f'{{ "message": "{sys.argv[1]}" }}' }, None))
