try:
    with open("PYTHON/reference/File/fileToRead.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found")
