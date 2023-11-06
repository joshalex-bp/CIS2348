#Joshua Guajardo   PSID: 1811892


string_input = input()
list_string = string_input.split(" ")

for i in range(0, len(list_string)):
    count = 0
    for h in range(0, len(list_string)):
        if(list_string[i]==list_string[h]):
            count += 1
    print(list_string[i], str(count))
