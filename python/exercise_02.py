#2. Iterate through the first 10 numbers (0–9).
#In each iteration, print the current number, the previous number,
# and their sum.
numbers = range(10)
prev_num = 0
for num in numbers:
    num_sum = num + prev_num
    print("Current number ", num, "Previous Number", prev_num, "Sum:", num_sum)
    prev_num = num
    