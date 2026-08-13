# 6.	Convert temperatures from Celsius to Fahrenheit using map().
# •	Formula:
# •	F = (C * 9/5) + 32
#

a = [10,20,30,40,60]

l = list(map(lambda x: (x*9/5)+32,a))
print(l)