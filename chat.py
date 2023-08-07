import os
import chat

chat.api_key = "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"

completion = chat.chatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"user", "content":"Hello!"}
    ]
)

print(completion.choices[0].message.content)