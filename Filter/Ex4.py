# Filter strings with length greater than 4 from a list.
a = ["dewfs","aca","jjsw"]

l = list(filter(lambda x: len(x)>4,a))

print(l)