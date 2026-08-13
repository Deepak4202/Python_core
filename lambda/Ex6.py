# 6.	Use lambda to create a function that returns:
# •	"Positive" if number > 0
# •	"Negative" if number < 0
# •	"Zero" otherwise


pnz = lambda number :"Positive" if number > 0 else "Negative" if number < 0 else "Zero"

print(pnz(0))