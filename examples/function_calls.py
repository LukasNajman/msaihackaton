import json
from pprint import pp
from typing import List
from oai import get_chat_client
from openai.types.chat import ChatCompletionToolParam, ChatCompletionMessageParam
from openai.types.shared_params import FunctionDefinition

client = get_chat_client()


## A function that can be called and provide
def get_greeting(language: str) -> str:
    language = language.lower()
    if language == "english":
        return "Hello!"
    elif language == "spanish":
        return "¡Hola!"
    elif language == "french":
        return "Bonjour!"
    elif language == "german":
        return "Hallo!"
    elif language == "italian":
        return "Ciao!"
    elif language == "portuguese":
        return "Olá!"
    elif language == "ukrainian":
        return "Привіт!"
    elif language == "chinese":
        return "你好!"
    elif language == "japanese":
        return "こんにちは!"
    elif language == "korean":
        return "안녕하세요!"
    elif language == "arabic":
        return "مرحبا!"
    elif language == "czech":
        return "Ahoj!"
    else:
        return "Hello!"


## A helper function that calls the function based on its name
def call_function(function_name: str, arguments: dict) -> str:
    if function_name == "get_greeting":
        return get_greeting(**arguments)
    else:
        raise ValueError(f"Unknown function: {function_name}")


## Function description in OAI format
get_greeting_function_description: FunctionDefinition = {
    "name": "get_greeting",
    "description": "This function returns a greeting in the specified language. Supported languages are English, Spanish, French, German, Italian, Portuguese, Ukrainian, Chinese, Japanese, Korean, Arabic, and Czech.",
    "parameters": {
        "type": "object",
        "properties": {
            "language": {
                "type": "string",
                "description": "The language in which the greeting should be returned.",
            },
        },
        "required": ["language"],
        "additionalProperties": False,
    },
}

## Definition of tools that can be called by GPT
tools: List[ChatCompletionToolParam] = [
    {"type": "function", "function": get_greeting_function_description}
]


## Chat messages
messages: List[ChatCompletionMessageParam] = [
    {
        "role": "system",
        "content": "You are an assistant who greets users in their native language.",
    },
    {"role": "user", "content": "Hi GPT, I am Lukas and I am from Italy."},
]


## First call to the GPT, we expect tool_call
response = client.chat.completions.create(
    model="gpt-4o", messages=messages, tools=tools
)

pp(response)

## Check wheher the tool (fucntion) call was requested
if response.choices[0].finish_reason == "tool_calls":

    tool_calls = response.choices[0].message.tool_calls
    if tool_calls is None:
        raise ValueError("Expected tool calls in the response.")

    ## Extract tool call id, tool name and call arguments
    tool_call_id = tool_calls[0].id
    function = tool_calls[0].function
    arguments = json.loads(function.arguments)

    ## Invoke the tool
    fun_result = call_function(function.name, arguments)
    print("Function result:", fun_result)

    ## Add assistant tool call message and response with the tool call value into messages
    messages.extend(
        [
            response.choices[0].message,  # type: ignore
            {
                "role": "tool",
                "content": json.dumps({"greeting": fun_result}),
                "tool_call_id": tool_call_id,
            },
        ]
    )

    ## Second call to GPT
    response = client.chat.completions.create(
        model="gpt-4o", messages=messages, tools=tools
    )

    pp(response)
    print("GPT:", response.choices[0].message.content)
else:
    print(f"Tool_call not requetsed. Response: {response.choices[0].message.content}")
