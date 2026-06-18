#4.Write a function to remove characters
#from a string starting from index 0
# up to n and return a new string.
def remove_chars(string_var,n):
    return string_var[n:]
print(remove_chars("pynative",4))
print(remove_chars("pynative",2))