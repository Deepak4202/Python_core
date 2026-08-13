#subarraysum
def sumArray(arr):
    sums = 0
    c = 0
    for i in arr:
        c += i
        sums = max(c,sums)
        if c <1:
            c = 0

    return sums
print(sumArray([2, 3, -8, 7, -1, 2, 3]))