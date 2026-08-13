# 6.	Write a generator that yields only digits present in a string.

def onlyNumbers(n:str):

    for i in n:
        if i.isdigit():

            yield i

s = input('Enter a string with numbers:')
a = onlyNumbers(s)

for i in a:
    print(i)