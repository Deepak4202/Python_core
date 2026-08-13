#[10,40,2,4,14,42,42]
def SecondLargestElement(a):
    first = float("-inf")
    second = float('-inf')
    l = len(a)
    if l <2:
        return -1
    else:
        for i in a:
            if i > first :
                second = first
                first = i
            elif i >second and i != first:
               second = i
        else:
            if second == float("-inf"):
                return -1
            else:
                return second


a = [int(val) for val in input().split(",")]
print(SecondLargestElement(a))