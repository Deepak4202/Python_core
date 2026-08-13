#palindrome.py

#Write a Python program to check whether a number is palindrome or not.
# try:
#     a= int(input("Enter a number : "))
# except ValueError:
#     print("Dont enter alnums , alphabets and spacial character")
# else:
#     if str(a) == str(a)[::-1]:
#         print("palindrome")
#     else:
#         print("Not palindrome")

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")

    c = a + b
    a,b = b,c

