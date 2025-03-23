import openai
from openai import OpenAI

client = OpenAI(
  api_key=""
)

def generate_output(input):
    messages= [
        {
            "role" : "System",
            "content" : "Provide movie cast details for the user input movie name \n"

        }
    ]
    messages.append({"role": "user", "content" : f"{input}"})
    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        store = True,
        messages = messages
    )
    reply = completion.choices[0].message
    return reply
