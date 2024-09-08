import base64
from pprint import pprint
from oai import get_chat_client

client = get_chat_client()

image = open("./resources/starship.jpg", "rb").read()
base64_image = base64.b64encode(image).decode("utf-8")


chat_completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": """
                        You are an assistant that describes images the user supplies to you.
                        Be brief, but try to cover the whole picture with your description.
                        """,
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                }
            ],
        },
    ],
)
print(f"GPT: {chat_completion.choices[0].message.content}")

pprint(chat_completion.to_dict())
