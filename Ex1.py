
def prime(n):
    fc =0
    for i in range(1,n+1):
        if n%i==0:
            fc +=1
    if fc ==2:
        return True
    return False

def afer(a):

    a+=1

    if a>0:
        while True:
            if prime(a):
                af = a
                return af
            a+=1

def before(a):
    a -= 1

    if a > 0:
        while True:
            if prime(a):
                bp = a
                return bp
            a -= 1

a = int(input())
count =0

ap = afer(a)
bp = before(a)

ac = a - ap
bc = bp - a

if bp < ap:
    print(bp)
else:
    print(bp)