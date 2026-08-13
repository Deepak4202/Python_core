a = int(input("Enter a number"))

if a <=1:
    print("Invalid number")
elif a == 2:
    print("Prime number")
else:
    flag = True
    for i in range(2,a):
        if a%i == 0:
            flag = False
            print("Not prime")
            break
    else:
        if flag:
            print("prime")
