# 3.Display only those characters which 
# are present at an even index number in given string.
orig_str = input('Input origin string: ')
print('Origin string is ', orig_str)
print('Printing only even index chars')
start = 0
step = 2
even_chars = orig_str[start::step]
for char in even_chars:
        print(char)