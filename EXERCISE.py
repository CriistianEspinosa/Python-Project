import math

def raiz(number):
    if number < 0:
        return "You cannot calculate the square root of a negative number."
    else:
        return math.sqrt(number)

number = float(input("Enter a number to calculate its square root: "))

result = raiz(number)
print(result)
