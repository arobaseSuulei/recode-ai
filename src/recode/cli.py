def main():
    print("hello from there")

    while True:
        r=input(">")

        if r.lower() in ("exit","quit","q"):
            print("Goodbye")
            break
        print(f"You said {r}")



if __name__=="__main__":
    main()
