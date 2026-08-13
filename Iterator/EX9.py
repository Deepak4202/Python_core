# 2. Handle StopIteration
#
# Write a program to:
#
# Create an iterator for a tuple.
# Print all elements using next().
# Catch the StopIteration exception when the iterator is exhausted.

l = (int(val) for val in [10,20,30,40])
print(next(l))
try:
    while True:
        print(next(l))

except StopIteration as sp:
    print("Iterator is exhausted.")