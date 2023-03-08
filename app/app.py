import os
import openai

def handler(event, context):
    input = event.get("input")
    if not input:
        return ""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": os.getenv("GPT_CONTEXT", default="")},
            {"role": "user", "content": input},
        ]
    )
    message = response["choices"][0]["message"]["content"]
    return message
