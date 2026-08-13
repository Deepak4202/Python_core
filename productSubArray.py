def product(arr):
    maxa = float("-inf")
    for i in range(len(arr)):
        c = 1
        for j in range(i,len(arr)):
            c *= arr[j]
            maxa = max(maxa,c)
    return maxa

print(product([-2, 6, -3, -10, 0, 2]))