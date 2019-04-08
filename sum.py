"""This program will sum all even integers from 2 to 100."""

sum = 0

for number in range(2, 101, 2):
    sum = sum + number

print("Sum is %d" % sum)