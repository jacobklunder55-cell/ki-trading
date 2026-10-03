from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)

messages = [
    {
        "role": "system",
        "content": "Du bist ein hilfreicher Assistent."
    }
]

while True:
    user_input = input("\nDu: ")

    if user_input.lower() in ["exit", "quit", "ende"]:
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model="local-model",
        messages=messages
    )

    answer = response.choices[0].message.content

    print(f"\nKI: {answer}")

    messages.append({
        "role": "assistant",
        "content": answer
    })
