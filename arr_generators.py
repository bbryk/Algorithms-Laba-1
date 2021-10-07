from random import randint,choice
def randomly_generated(power_size:int):
    arr = [randint(1,10**10) for i in range(2**power_size)]
    return arr

def ascending_order(power_size:int):
    arr = [i for i in range(2**power_size)]
    return arr

def descending_order(power_size:int):
    arr = [i for i in range(2 ** power_size, 0, -1)]
    return arr

def similar_values(power_size:int):
    arr = [choice([1,2,3]) for _ in range(2**power_size)]
    return arr



 # A = expirement(power_size)
 #            i = 0
 #            for algorithm in algorithms:
 #                B = deepcopy(A)
 #
 #                print(f"        {algorithm.__name__}\n")
 #                file_log.write(f"        {algorithm.__name__}\n")
 #                obj = algorithm()
 #
 #                if (i % 4 == 0):
 #                    res = []
 #                    for _ in range(5):
 #                        res.append(obj.selection_sort(B))
 #
 #                elif (i % 4 == 1):
 #                    res = []
 #                    for _ in range(5):
 #                        res.append(obj.insertion_sort(B))
 #                    counter
 #
 #                elif (i % 4 == 2):
 #                    res = []
 #                    for _ in range(5):
 #                        res.append(obj.mergeSort(B))
 #                    counter = obj.mergeSort(B)
 #                elif (i % 4 == 3):
 #                    counter = obj.shellsort(B)
 #                i += 1
 #                file_log.write(f"           {counter}\n")
