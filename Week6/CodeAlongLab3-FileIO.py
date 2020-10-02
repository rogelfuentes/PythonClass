while True:
    fileName = input("Enter a file name: ")
    try:
        fhandle = open(fileName, 'a')
        while True:
            text = input("What do you want to write out?")
            if text.lower() == "done":
                # fhandle.close()
                break
            fhandle.write(text + "\n")
    except Exception as exe:
        print(exe)
    else:
        break

