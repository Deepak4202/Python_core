def Longest_Subarray(s):   #0101010 output :6
    empty = {}
    for v in s:
        if v not in empty:
            empty[v] = 1
        else:
            empty[v] = empty[v]+1

    if empty['0'] == empty['1']:
        print(sum(empty.values()))
    elif empty['0'] > empty['1']:
        empty['0'] = empty['0'] - (empty['0'] - empty['1'])
        print(sum(empty.values()))
    elif empty['1'] > empty['0']:
        empty['1'] = empty['1'] - (empty['1'] - empty['0'])
        print(sum(empty.values()))
a = input()
Longest_Subarray(a)