# Write a program that calculates the factorial 
# of a given number (e.g., 5!) using a for loop.
num = int(input('Enter the number whose factorial you want to calculate '))
factorial = 1
for i in range(1, num+1):
    factorial *= i
print(f'The factorial of {num} is {factorial}')
