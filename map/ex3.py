# 3.	Use map() to find the cube of each number.

a = [10,20,30,40,50]
cu  = lambda b : b*b*b

l = list(map(cu ,a))
print(l)
