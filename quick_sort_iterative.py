# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# Function to do Quick sort
# arr[] --> Array to be sorted,
# l  --> Starting index,
# h  --> Ending index
def quickSortIterative(arr, l, h):
    # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * (size)

    # initialize top of stack
    top = -1

    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    print((f"starting stack {stack}\n"))

    # Keep popping from stack while is not empty
    i = 0
    while top >= 0:
        i +=1
        print(f"stack on {i} loop = {stack}")



        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        # Set pivot element at its correct position in
        # sorted array
        p = partition(arr, l, h)
        print(f"partition (q)  on loop {i} = {p} (value of partition = {arr[p]})")
        print(f"array at {i} loop = {arr}")
        print(f"relativaly to {arr[p]} sorted\n")
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


# Driver code to test above
arr = [4, 3, 8, 13, 6, 9, 10, 5]
print(f"arr =  {arr}")
n = len(arr)
quickSortIterative(arr, 0, n - 1)


# This code is contributed by Mohit Kumra