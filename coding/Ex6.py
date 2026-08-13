# 5. 92436 = 2+4+3
def count(n):
    c =0
    while n>0:
        c+=1
        n//=10
    return c
a = int(input())
def sum_of_middle_digits(n):
    f = a//10
    digit = count(f)
    r = f % (10**(digit-1))
    s=0
    while r>0:
        s += r %10
        r//=10
    return s
print(sum_of_middle_digits(a))
