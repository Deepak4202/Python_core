a = [12,15,18,20,21,25]

m = list(filter(lambda x: (x % 3 == 0 or x % 5 !=0)or (x % 3 != 0 or x % 5 ==0),a))

print(m)