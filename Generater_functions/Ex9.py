

def cumulative(l:list)->int:

    total =0
    for i in l:
        total+=i
        yield total

for i in cumulative([1,2,3,4,5,6]):
    print(i)