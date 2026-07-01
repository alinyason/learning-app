#Create a list of 5 fruits. Add a new fruit to the end of the list, 
#then remove the second fruit (at index 1)

fruits = ['apple', 'banana', 'pineapple', 'kiwi', 'orange']
print(f'list before change {fruits}')
fruits.append('avocado')
fruits.pop(1)
print(f'list after change {fruits}')