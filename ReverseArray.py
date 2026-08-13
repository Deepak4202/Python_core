def reverseArray(arr):
    print("Before:{}".format(arr))
    if len(arr) < 2:
        return arr
    # code here
    else:
        start = 0
        end = len(arr) - 1
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        return arr
a =reverseArray([231,3,1,4,13213,312,2])
print("After:{}".format(a))