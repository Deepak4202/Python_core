# 5.	Write a lambda function to find the maximum among three numbers.

max = lambda a,b,c : a if a>b and a>c else b if b > c and b>a else c

print(max( 0,0,30))