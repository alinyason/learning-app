# 3.Display only those characters which 
# are present at an even index number in given string.
orig_str = input('Input origin string: ')
print('Origin string is ', orig_str)
print('Printing only even index chars')
start = 0
stop = len(orig_str) #range не включает последнее число
step = 2
for index_char in range(start,stop,step):
        print(orig_str[index_char])