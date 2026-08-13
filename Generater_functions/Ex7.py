# 7.	Write a generator that yields the square of each element in a list.

a = (val*val for val in [1,2,3,4,5,6,7] )

for i in a:
    print(i)