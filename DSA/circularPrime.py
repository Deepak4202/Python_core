def isprime(n):
    fact = 0
    for i in range(1,n+1):
        if n % i ==0:
            fact+=1
    return fact == 2


def digitcount(n):

    c =0
    while n>0:
        c+=1
        n//=10
    return c

def cirular_prime(n):

    count = digitcount(n)
    flag = True

    for i in range(count):
        last  = n % 10

        n = last * (10**(count-1)) + n // 10

        print(n)

        if not isprime(n):
            flag =False
            break
    return flag


if cirular_prime(int(input())):
    print("Circular prime")
else:
    print("Not circular prime")