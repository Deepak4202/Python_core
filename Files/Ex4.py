# Write a program that opens a file in read mode,
# reads the first 10 characters,
# prints the current cursor position using tell(),
# moves the cursor back to the beginning using seek(0),
# and reads the full content again

with open("Test2.txt") as fp:

    a = fp.read(10)
    print(fp.tell())
    fp.seek(0)

    print(fp.read())
