import ollama

MODEL = "gemma3:4b"

SYSTEM_PROMPT = """
You are a helpful local AI assistant.
Answer clearly and accurately.
Remember the conversation context provided to you.
"""


def main():
    print("=" * 60)
    print("                 LOCAL AI ASSISTANT")
    print("=" * 60)
    print(f"Model: {MODEL}")
    print("Commands: 'reset' to clear memory, 'exit' to quit.\n")

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        }
    ]

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Assistant: Goodbye!")
            break

        if user_input.lower() == "reset":
            messages = [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                }
            ]
            print("Assistant: Conversation memory cleared.\n")
            continue

        if not user_input:
            continue

        messages.append(
            {
                "role": "user",
                "content": user_input,
            }
        )

        try:
            response = ollama.chat(
                model=MODEL,
                messages=messages,
            )

            assistant_content = response["message"]["content"]

            print(f"Assistant: {assistant_content}\n")

            messages.append(
                {
                    "role": "assistant",
                    "content": assistant_content,
                }
            )

        except Exception as e:
            print(f"Assistant Error: {e}\n")


if __name__ == "__main__":
    main()
