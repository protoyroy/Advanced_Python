def readFile(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f'File {filename} is not found')

readFile("Chapter 12/1.txt")
readFile("Chapter 12/5.txt")
readFile("Chapter 12/2.txt")
readFile("Chapter 12/3.txt")
readFile("Chapter 12/4.txt")