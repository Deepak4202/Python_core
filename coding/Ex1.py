# An Automorphic number is a number whose square ends with the same number itself.
#5² = 25 → ends with 5 ✔️
# 6² = 36 → ends with 6 ✔️
# # 25² = 625 → ends with 25
# 1.print nth prime number input =5 ,output = 11
# 2.find out given number is super number or not input = 153  1**1 +5**2 +3**3
# 3.Given number is emirp number or not
# 4.print the circular number of given number
# 5. 92436 = 2+4+3

# 6.9423 = 9+4+2+3 = 18 =1+8

a = int(input())
def dcount(n):
    c = 0
    while n > 0:
        c += 1
        n //= 10
    return c
def check(n):
    s =a**2
    dc = dcount(n)

    r = a%(10**dc)

    if r == n:
        return True

    return False

if check(a):
    print("Automorphic number")
else:
    print("not automorphic number")



