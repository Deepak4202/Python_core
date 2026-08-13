# 4.print the circular number of given number
# Right Rotation (your logic):
def prime(n):
    fc =0
    for i in range(1,n+1):
        if n %i == 0:
            fc +=1

    if fc ==2:
        return True
    return False


def dcount(n):
    cc =0
    while n>0:
        cc+=1
        n //=10
    return cc
def circularprime(a):
    if prime(a):
        c = dcount(a)
        for _ in range(c):
            r = a %10
            rotation = r * (10**(c-1)) + a//10

            a = rotation
            print(a)
            if not prime(a):
                return False
        return True
    return False

a = int(input("Enter a number : "))
if circularprime(a):
    print(f"{a} is a circular prime ")
else:
    print(f"{a} is not a circular prime ")

# left rotation
# def dcount(n):
#     c = 0
#     while n > 0:
#         c += 1
#         n //= 10
#     return c
#
# a = 3234
# c = dcount(a)
#
# for _ in range(c):
#     first = a // (10 ** (c - 1))
#     rest = a % (10 ** (c - 1))
#     a = rest * 10 + first
#     print(a)