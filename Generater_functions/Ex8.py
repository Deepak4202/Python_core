# 8.	Write a generator that yields digits from an integer one by one.
n = int(input())
a = ( val for val in str(n))


for i in a:
    print(i)