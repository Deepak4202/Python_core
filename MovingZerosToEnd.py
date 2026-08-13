#MovingZerosToEnd.py
"""You are given an array arr[] of non-negative integers.
You have to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements.
The operation must be performed in place, meaning you should not use extra space for another array.

Examples:

Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.
Input: arr[] = [10, 20, 30]
Output: [10, 20, 30]
Explanation: No change in array as there are no 0s.
Input: arr[] = [0, 0]
Output: [0, 0]
Explanation: No change in array as there are all 0s."""

def MoveZeros(a):

    #[1, 2, 0, 4, 3, 0, 5, 0]
    instpos =0
    for i in range(len(a)):
        if a[i] != 0:
            print("Before InsertionPosition:{}".format(instpos))
            print("i = {}".format(i))
            a[instpos] = a[i]
            instpos +=1
            print(a)
            print("After InsertionPosition:{}".format(instpos))
    else:
        while instpos < len(a):
            a[instpos] = 0
            instpos +=1
        return a

print(MoveZeros([1, 2, 0, 4, 3, 0, 5, 0]))

"""
Before InsertionPosition:0
i = 0
[1, 2, 0, 4, 3, 0, 5, 0]
After InsertionPosition:1
Before InsertionPosition:1
i = 1
[1, 2, 0, 4, 3, 0, 5, 0]
After InsertionPosition:2
Before InsertionPosition:2
i = 3
[1, 2, 4, 4, 3, 0, 5, 0]
After InsertionPosition:3
Before InsertionPosition:3
i = 4
[1, 2, 4, 3, 3, 0, 5, 0]
After InsertionPosition:4
Before InsertionPosition:4
i = 6
[1, 2, 4, 3, 5, 0, 5, 0]
After InsertionPosition:5
[1, 2, 4, 3, 5, 0, 0, 0]
"""