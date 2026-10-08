# Write a program that opens a file using a context manager,
# reads all lines using readlines(),
# and prints only the lines that contain more than 10 characters

with open("test.txt","r") as f:
    a = f.readlines()
    for i in a:

        if len(i.strip()) >10:
            print(i.strip())
