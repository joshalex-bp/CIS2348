# Joshua Guajardo   PSID: 1811892
num_calls = 0

def partition(user_ids, i, k):
    #using the binary search
    index = (i + k) // 2
    value = user_ids[index]

    #set the high and low values
    j = i
    f = k

    while True:

        #find the element that is greater on the left in the list
        while user_ids[j] < value:
            j += 1
        #find the element that is smaller on the right in the list
        while user_ids[f] > value:
            f -= 1

        #checks if the high and low values are same then return the high
        if j >= f:
            return f

        #swapping the high and low
        user_ids[j], user_ids[f] = user_ids[f], user_ids[j]

        j += 1
        f -= 1


def quicksort(user_ids, i, k):
    global num_calls
    num_calls += 1

    if i < k:
        # Partition the list
        partition_index = partition(user_ids, i, k)

        # Recursively sort the low and high partitions
        quicksort(user_ids, i, partition_index)
        quicksort(user_ids, partition_index + 1, k)

if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)