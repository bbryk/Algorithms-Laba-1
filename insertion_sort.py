def insertion_sort(unsorted_list: list):
    counter = 0
    length = len(unsorted_list)

    for i in range(1, length):
        key = unsorted_list[i]
        j = i - 1
        counter +=2
        while j >= 0 and unsorted_list[j] > key:  # practically more eefective then bubble
            counter += 2
            unsorted_list[j + 1] = unsorted_list[j]
            unsorted_list[j] = key
            j -= 1

    return counter
