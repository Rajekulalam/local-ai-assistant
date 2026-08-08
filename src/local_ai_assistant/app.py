import ollama


MODEL = "gemma3:4b"


def main():
    print("=" * 60)
    print("              LOCAL AI ASSISTANT")
    print("=" * 60)
    print(f"Model: {MODEL}")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Assistant: Goodbye!")
            break

        if not user_input:
            continue

        try:
            response = ollama.chat(
                model=MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": user_input,
                    }
                ],
            )

            print(f"Assistant: {response['message']['content']}\n")

        except Exception as e:
            print(f"Assistant Error: {e}\n")


if __name__ == "__main__":
    main()
