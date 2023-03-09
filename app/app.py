import os
import sys
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
    if sys.argv.length < 1:
        print("Usage: python app.py <input>")
        sys.exit(1)
    print(handler({"input": sys.argv[1]}, None))
