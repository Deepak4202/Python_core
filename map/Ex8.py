def isprime(n):
    fc = 0
    for i in range(1,n+1):
        if n % i == 0:
            fc += 1
    if fc == 2:
        return True
    return False
n = int(input())

l = []
i =2
for i in range(2,n+1):
    if n % i  == 0:
        if isprime(i):
            l.append(i)

print(l)