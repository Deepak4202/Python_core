# isvowels.py
# Write a Python program to count number of vowels in a string
a = input("Enter a string")

b = ['a','A','E','e','i','I','o','O','U','u']
count =0
for i in a:
    if i in b:
        count +=1
else:
    print("Number of vowels in '{}'= {}".format(a,count))