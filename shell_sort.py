
def shell_sort(arr):
    сounter = 0
    n = len(arr)
    gap = n // 2
    сounter+=1
    while gap > 0:
        сounter+=1
        for i in range(gap, n):
            temp = arr[i]
            j = i
            сounter+=2
            while j >= gap and arr[j - gap] > temp:
                сounter+=2
                arr[j] = arr[j - gap]
                j = j - gap
            arr[j] = temp
        gap = gap // 2
    return сounter

if __name__=="__main__":

    print(shell_sort([23,1,34,65,12,939,3,4,18,9,4]))
