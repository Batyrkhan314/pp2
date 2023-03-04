'''Write a Python program to copy the contents of a file to another file '''

with open("text.txt") as f:
    with open("items.txt", "w") as f1:
        for line in f:
            f1.write(line)
