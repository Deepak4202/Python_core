# 5.	Write a generator that yields only vowels from a string.

def Vowels(n:str):
    for i in range(1,len(n)+1):
        if n[i].lower() in "aeiou":
            yield n[i]

a = Vowels(input())


