from recode.agent import create_agent
    

def main():
    agent=create_agent()
    
    print("-- Recode.ai, What are we going to build chief --")
    while True:
        user_input=input("> ")
        if user_input.lower() in ("exit","quit"):
            break
        result=agent.run(user_input,reset=False)
        print(result)
        
if __name__ == "__main__":
    main()