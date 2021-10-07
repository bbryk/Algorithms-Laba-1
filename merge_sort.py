def merge_sort( arr, counter=0):
    counter += 1
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]

        R = arr[mid:]

        counter += merge_sort(L)

        counter += merge_sort(R)

        i = j = k = 0

        counter += 2
        while i < len(L) and j < len(R):
            counter += 2
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        counter +=1
        while i < len(L):
            counter += 1
            arr[k] = L[i]
            i += 1
            k += 1
        counter +=1
        while j < len(R):
            counter += 1
            arr[k] = R[j]
            j += 1
            k += 1
    return  counter

