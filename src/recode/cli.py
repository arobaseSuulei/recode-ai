from recode.harness import Harness

def main():
    print("hello from there")
    while True:
        r=input("> ")
        if(r.lower() in ("exit","quit","q")):
            print("Goodbye.")
            break
        response=Harness()
        res=response.handle(r)
        print(res)

if __name__=="__main__":
    main()


    
