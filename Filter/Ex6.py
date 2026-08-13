s = input("Enter a string: ")

vowels = "".join(filter(lambda ch: ch.lower() in "aeiou", s))

print("Vowels:", vowels)

from functools import reduce as re

a = [10,20,30]
r  = re(lambda x,v: x if x>v else v,a)
print(r)