from agent import create_agent

def main():
    while True:
        prompt = input("> ")

        res=create_agent(prompt)

        if prompt in ("exit", "q"):
            break

        for event in res:
            if event["type"]=="loading_memory":
                print(event["text"])
            if event["type"]=="start":
                print("model thinking")
            if event["type"]=="text_delta":
                print(event["text"],end="",flush=True) 
            if event["type"]=="completed":
                print("finish")
            
                

        
        #print(f"Token Output : {response.usage.output_tokens}")


if __name__ == "__main__":
    main()
