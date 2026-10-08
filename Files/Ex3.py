# Write a program that creates a file and writes 3 lines using write(),
# reopens the same file in append mode, appends 2 more lines,
# and finally reads and prints the complete file content

with open("Test2.txt","w") as f:

    f.write("Deepak\n")
    f.write("I love python\n")
    f.write("Bye every one\n")

with open("Test2.txt","a+") as fp:

    fp.write("line1 using append\n")
    fp.write("line2 using append\n")
    fp.seek(0)
    s = fp.read()
    print(s)


