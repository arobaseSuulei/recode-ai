from agent import create_agent

def main():
    while True:
        prompt = input("> ")

        if prompt in ("exit", "q"):
            break

        response = create_agent(prompt)
        print(response.output_text)
        print(f"Token Output : {response.usage.output_tokens}")


if __name__ == "__main__":
    main()
