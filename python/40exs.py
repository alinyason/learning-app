#Write a Python function that accepts two integer numbers. 
#If the product of the two numbers is less than or equal to 1000
# return their product; otherwise, return their sum.

number1 = float(input("Input number1: "))
number2 = float(input("Input number2: "))
def Exs1(num1,num2):
    if num1 * num2 <= 1000:
        itog = num1 * num2
    else: itog = num1 + num2
    return itog
result = Exs1(number1, number2)
print(result)