#Joshua Guajardo    PSID:1811892

def selection_sort_descend_trace(num): #function to sort inputs
    for i in range(len(num) - 1): #goes through the list except the last one

        #current index is the minimum
        u = i
        for j in range(i + 1, len(num)):  #iterate through the unsorted list

            if num[u] < num[j]: # if one number is bigger than another update it
                u = j

         #swap elements of list
        num[i], num[u] = num[u], num[i]


        for value in num: #printing out the values
            print(value,end=" ")
        print()

    return num

if __name__ == "__main__":
    num = []
            #reading list of integers from user input
    num = [int(x) for x in input("").split()]
    selection_sort_descend_trace(num)
