# 5.	Write a function full_name(first, last) that returns complete name

def full_name(first , last):
    return first ,last


a = full_name(input("Enter your first name : "),input("Enter your second name : "))
print("{} {}".format(a[0],a[1]))