# 1.	Use map() with a lambda function to add 5 to every element.
a = [10,20,30,40,50]
add = lambda b : b+5

l = list(map(add ,a))
print(l)
