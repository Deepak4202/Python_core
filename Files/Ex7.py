# Write a program using a context manager that opens a file in read mode,
# uses a loop to read the file in small chunks (for example, 5 characters at a time),
# prints the cursor position after each read using tell(),
# uses seek() to move to a specific position,
# and continues reading from there


with open("Test2.txt",'r') as fp :

    while True:

        a = fp.read(10)
        if a == "":
            break

        print(a.strip())
        print(fp.tell())

    fp.seek(10)
    print(fp.read(5))

