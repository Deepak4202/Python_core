# 3.Given number is emirp number or not
def prime(n):
    fc = 0
    for  i in range(1,n+1):
        if n % i ==0:
            fc +=1
    if fc ==2:
        return True
    return False
def reverse(n):
    s=0
    temp =n
    while n >0:
        r = n %10
        s = s*10 +r
        n //=10


    if prime(s):
        print(f"{temp} is Emirp number")
    else:
        print(f"{temp} is not Emirp Number")

reverse(int(input("Enter a number : ")))