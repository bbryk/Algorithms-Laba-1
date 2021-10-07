def selection_sort(arr: list):
    counter = 0

    for i in range(len(arr)):

        min_idx = i
        for j in range(i + 1, len(arr)):
            counter += 1
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return counter

