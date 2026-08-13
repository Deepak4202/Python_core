# 12.	 Filter numbers divisible by 5 from a list.

a = [10,22,15,16,25,35,25]

l = list(filter(lambda x : x % 5 == 0 ,a))
print(l)