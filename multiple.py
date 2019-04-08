"""Write a program that reads in two integers and determines and prints whether
the first is a multiple of the second. (Hint: Use the modulus operator)"""

integer1 = input("Enter first integer: ")
integer1 = int(integer1)

integer2 = input("Enter second integer: ")
integer2 = int(integer2)

if integer1 % integer2 == 0:
    print("%d is a multiple of %d" % (integer1, integer2))