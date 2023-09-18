# Joshua Guajardo    PISD:1811892

# Requesting an integer from user and printing out that input
user_num = int(input('Enter integer:\n'))
print('You entered:', user_num)

# Calculating the square of the input and printing the result
user_num_sq = user_num * user_num
print(user_num, 'squared is', user_num_sq)

# Calculating the cube of the input and printing the result
user_num_cu = user_num * user_num * user_num
print('And', user_num, 'cubed is', user_num_cu, '!!')

# Requesting another integer from the user
user_num2 = int(input('Enter another integer:\n'))

# Calculating the sum and product of both inputs requested
sum_1 = user_num + user_num2
pro_1 = user_num * user_num2

# Printing the answer of the calculation
print(user_num, '+', user_num2, 'is', sum_1)
print(user_num, '*', user_num2, 'is', pro_1)