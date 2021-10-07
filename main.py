from time import perf_counter_ns
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort  import merge_sort
from shell_sort import shell_sort
from copy import deepcopy
from arr_generators import  randomly_generated, ascending_order, descending_order, similar_values






expirements  = [randomly_generated, ascending_order, descending_order, similar_values]
algorithms = [selection_sort, insertion_sort, merge_sort, shell_sort]

with open("log.txt", 'w') as file_log:

    for i in range(4):

        file_log.write(f"Expiremrnt: {expirements[i].__name__}\n")
        for power_size in range(7,16):
            file_log.write(f"   powersize: {power_size}\n")
            for algorithm in algorithms:
                file_log.write(f"       alrorithm: {algorithm.__name__}\n")
                res_com = []
                res_time = []
                if i == 0:
                    for _ in range(5):
                        A = expirements[i](power_size)
                        B = deepcopy(A)
                        st_time = perf_counter_ns()
                        res_com.append(algorithm(B))
                        fn_time = perf_counter_ns()
                        a_time = fn_time - st_time
                        res_time.append(a_time)
                    avarage = sum(res_com)//5
                    a_time = sum(res_time)//5
                else:
                    A = expirements[i](power_size)
                    B = deepcopy(A)
                    st_time = perf_counter_ns()
                    avarage = algorithm(B)
                    fn_time = perf_counter_ns()
                    a_time = fn_time - st_time

                file_log.write(f"           counter: {avarage}\n")
                file_log.write(f"           time: {a_time}\n")












