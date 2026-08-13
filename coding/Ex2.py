# 1.print nth prime number input =5 ,output = 11


a = int(input("Enter nth number : "))
def checkprime(n):
    fc = 0
    for i in range(1,n+1):
        if n % i == 0:
            fc += 1

    if  fc  == 2:
        return True
    return False
s = 1
c =0
while True:
    if checkprime(s):
        c += 1
        if c ==a:

            print(f"{a} prime is : {s}")
            break


    s +=1
