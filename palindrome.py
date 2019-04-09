"""Write a program that reads a five-digits integer and determines whether it is a palindrome
(Hint: use the division and modulus operators to separate the number into its individual digits)"""

number = input("Enter a five-digits number: ")

number = int(number)

digit1 = number // 10000

number = number % 10000

digit2 = number // 1000

number = number % 1000

digit3 = number // 100

number = number % 100

digit4 = number // 10

number = number % 10

digit5 = number

print(digit1 , "\t", digit2, "\t", digit3, "\t", digit4, "\t", digit5)

if digit1 == digit5 and digit2 == digit4:
    print("The number you entered is a palindrome")
else:
    print("The number you entered is not a palindrome")