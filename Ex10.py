s = input()

numbers = []
num = ""

for i in range(len(s)):

    if s[i].isdigit():
        num += s[i]

    else:
        if num:
            numbers.append(num)
            num = ""

        if s[i] == "-":
            num = "-"

if num:
    print(num)
    numbers.append(num)

total = 0

for n in numbers:
    total += int(n)

expression = ""

for n in numbers:
    if n.startswith("-"):
        expression += n
    else:
        if expression:
            expression += "+"
        expression += n

print(expression + "=" + str(total))