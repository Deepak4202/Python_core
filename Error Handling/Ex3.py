# Write a function named find_length(obj) that uses a loop to
# calculate the length of the given object without using the built-in len() function.
# The function should return the calculated length if the object is iterable.
# If a non-iterable object such as an integer is passed,
# the function should raise and handle a TypeError, and print an appropriate error message explaining
# what happens when an integer is sent as input.

def find_length(obj):
    try:
        count = 0

        for i in obj:
            count += 1

        return count

    except TypeError:
        print("TypeError: The given object is not iterable.")
        print("An integer cannot be iterated because it is not an iterable object.")


# Examples
print(find_length("Hello"))
print(find_length([10, 20, 30, 40]))
find_length(10)