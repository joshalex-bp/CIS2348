#Joshua Guajardo    PSID:1811892


user_input = input()
user_list = user_input.split()

num_list = []
for num in user_list:
    pos_num = int(num)
    num_list.append(pos_num)

new_list = []

for i in num_list:
    if i >= 0:
        new_list.append(i)

new_list.sort()


for x in new_list:
    print(x, end=" ")



