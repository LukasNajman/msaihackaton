from oai import get_chat_client

if __name__ == '__main__':
    client = get_chat_client()
    with open("../resources/report.md", "r") as file:
        content = file.read()

        message = "Summarize this document: \n" \
                    f"{content}"

        chat_completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Your task is to summarize the markdown document that was given to you."
                                              " The document lists important comodity market evets that happend in the last 24 hours. "},
                {"role": "user", "content": message},
            ],
        )
        print(chat_completion.choices[0].message.content)

