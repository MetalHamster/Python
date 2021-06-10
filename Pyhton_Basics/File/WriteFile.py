text = "hihihi\nhahaha\n"

# Will overrite file
with open("PYTHON/reference/File/fileToWrite.txt", "w") as file:
    file.write(text)

newtext = "I will be appended"

# Append to a file
with open("PYTHON/reference/File/fileToWrite.txt", "a") as file:
    file.write(newtext)
