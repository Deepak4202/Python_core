# 7.	Use map() to check whether numbers are even or odd.

a = [1,2,3,4,5,6,7,8,9]

l = list(map(lambda x: "even" if x % 2 == 0  else "odd",a))

for i,v in zip(a,l):
    print("{}------->{}".format(i,v))