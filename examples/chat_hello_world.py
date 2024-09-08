from pprint import pp
from openai import AzureOpenAI
from oai import get_chat_client

client = get_chat_client()

message = "Hi GPT, please, tell me a joke."

chat_completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are helpfull and kind assistant."},
        {"role": "user", "content": message},
    ],
)
print(f"I: {message}")
print(f"GPT: {chat_completion.choices[0].message.content}")

pp(chat_completion.to_dict())
