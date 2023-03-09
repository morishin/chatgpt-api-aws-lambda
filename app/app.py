import os
import openai

def handler(event, context):
    input = event.get("input")
    if not input:
        return ""
    gpt_context = os.getenv("GPT_CONTEXT", default="")
    print("GPT_CONTEXT", gpt_context)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": gpt_context},
            {"role": "user", "content": input},
        ]
    )
    message = response["choices"][0]["message"]["content"]
    return message

if __name__ == "__main__":
    print(handler({"input": "Hello"}, None))
