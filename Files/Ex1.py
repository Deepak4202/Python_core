# Write a Python program using a context manager (with) to open a text file in read mode,
# read the entire content using read(),
# and print the number of characters in the file.
with open("test.txt", "w",newline='\n') as f:
    f.write("hi my name is deepak")
    print(f.tell())
    f.write("hi my name is deepak")

with open("test.txt", "a",newline='\n') as f:
    f.write("hi my name is deepak")
    f.write("hi my name is deepak")


with open("test.txt","r") as f:

    a = f.read()
    print(len(a))
