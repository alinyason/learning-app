#5.Write a program to swap the values of two variables
# a and b
# without using a third temporary variable
a = 5
b = 10
print(f"Before swap: a = {a},b = {b}")
# Simultaneous assignment (Tuple Unpacking)
a, b = b, a
print(f"After swap: a = {a},b = {b}")