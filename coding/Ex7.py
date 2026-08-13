# 6.  9423 = 9+4+2+3 = 18 =1+8
n = int(input())

while n>9:
    total =0
    while n>0:
        total += n%10
        n//=10
    n =total

print(n)

# n = int(input())
#
# if n == 0:
#     print(0)
# else:
#     print(1 + (n - 1) % 9)
