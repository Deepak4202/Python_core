# Given a string s containing only the characters '(', ')', '{', '}', '[', and ']',
# determine whether the input string is valid.

def validString(n: str) -> bool:
    es = []

    for i in n:

        if i in "({[":
            es.append(i)

        else:
            if not es:
                return False

            top = es.pop()

            if i == ')' and top != '(' or \
               i == '}' and top != '{' or \
               i == ']' and top != '[':
                return False

    return len(es) == 0


s = input()
print(validString(s))