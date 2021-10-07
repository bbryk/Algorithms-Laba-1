import pylab
import matplotlib.pyplot as plt

powersizes = [i for i in range(7,16)]
randomly_generated = {'selection_sort':[[],[]], 'insertion_sort':[[],[]], 'merge_sort':[[],[]], 'shell_sort':[[],[]]}
ascending_order = {'selection_sort':[[],[]], 'insertion_sort':[[],[]], 'merge_sort':[[],[]], 'shell_sort':[[],[]]}
descending_order = {'selection_sort':[[],[]], 'insertion_sort':[[],[]], 'merge_sort':[[],[]], 'shell_sort':[[],[]]}
similar_values = {'selection_sort':[[],[]], 'insertion_sort':[[],[]], 'merge_sort':[[],[]], 'shell_sort':[[],[]]}

with open('log.txt') as file_to_read:
    lines = file_to_read.readlines()

    for i in range(0,117):
        for key in randomly_generated.keys():
            if lines[i].split()[-1] ==key:
                c = int(lines[i+1].split()[-1])
                t = int(lines[i+2].split()[-1])
                randomly_generated[key][0].append((c))
                randomly_generated[key][1].append(t)
    for i in range(118,235):
        for key in ascending_order.keys():
            if lines[i].split()[-1] ==key:
                c = int(lines[i+1].split()[-1])
                t = int(lines[i+2].split()[-1])
                ascending_order[key][0].append((c))
                ascending_order[key][1].append(t)
    for i in range(236,353):
        for key in descending_order.keys():
            if lines[i].split()[-1] ==key:
                c = int(lines[i+1].split()[-1])
                t = int(lines[i+2].split()[-1])
                descending_order[key][0].append((c))
                descending_order[key][1].append(t)
    for i in range(354,471):
        for key in similar_values.keys():
            if lines[i].split()[-1] ==key:
                c = int(lines[i+1].split()[-1])
                t = int(lines[i+2].split()[-1])
                similar_values[key][0].append((c))
                similar_values[key][1].append(t)





#     print(lines[118])
#     print(lines[236])
#
# #
for key in randomly_generated.keys():
    print(len(randomly_generated[key][0]))
    print(len(randomly_generated[key][1]))
    print('\n')
    print(len(ascending_order[key][0]))
    print(len(ascending_order[key][1]))
    print('\n')
    print(len(descending_order[key][0]))
    print(len(descending_order[key][1]))
    print('\n')
    print(len(similar_values[key][0]))
    print(len(similar_values[key][1]))







# ax.set_yscale('log')


#randomly generated:
# fig = plt.figure()
# ax = fig.add_subplot(2, 1, 1)
# for key in randomly_generated.keys():
#     line, = ax.plot(powersizes, randomly_generated[key][0], color='blue', lw=1, label = key)
#
#
# ax.set_yscale('log')
#
# pylab.show()

def randomly_generated_comparisons():
    colors = ['blue','red','yellow','green']
    i = 0
    for key in randomly_generated.keys():

        plt.plot(powersizes, randomly_generated[key][0],color=colors[i], label =key )
        i+=1
    plt.title("Randomly generated array")
    plt.yscale('log')
    plt.ylabel('Y :Number of comparisons (logarithmic scale)')
    plt.xlabel('X : Powersizes')

    plt.legend()
    plt.show()

def randomly_generated_time():
    colors = ['blue', 'red', 'yellow', 'green']
    i = 0
    for key in randomly_generated.keys():
        plt.plot(powersizes, randomly_generated[key][1], color=colors[i], label=key)
        i += 1

    plt.title("Randomly generated array")
    plt.yscale('log')
    plt.ylabel('Y : Time (in nanoseconds) (logarithmic scale)')
    plt.xlabel('X : Powersizes')

    plt.legend()
    plt.show()
#ascending_order, descending_order, similar_values
def ascending_order_comparisons():
    colors = ['blue', 'red', 'yellow', 'green']
    i = 0
    for key in ascending_order.keys():
        plt.plot(powersizes, ascending_order[key][0], color=colors[i], label=key)
        i += 1

    plt.title("Ascending-ordered array")
    plt.yscale('log')
    plt.ylabel('Y :Number of comparisons (logarithmic scale)')
    plt.xlabel('X : Powersizes')
    plt.legend()

    plt.show()

def ascending_order_time():
    colors = ['blue', 'red', 'yellow', 'green']
    i = 0
    for key in ascending_order.keys():
        plt.plot(powersizes, ascending_order[key][1], color=colors[i], label=key)
        i += 1

    plt.title("Ascending-ordered array")
    plt.yscale('log')
    plt.ylabel('Y : Time (in nanoseconds) (logarithmic scale)')
    plt.xlabel('X : Powersizes')
    plt.legend()
    plt.show()

def descending_order_comparisons():
    colors = ['blue', 'red', 'yellow', 'green']
    i = 0
    for key in descending_order.keys():
        plt.plot(powersizes, descending_order[key][0], color=colors[i], label=key)
        i += 1

    plt.title("Descending-ordered array")
    plt.yscale('log')
    plt.ylabel('Y :Number of comparisons (logarithmic scale)')
    plt.xlabel('X : Powersizes')
    plt.legend()

    plt.show()

def descending_order_time():
    colors = ['blue', 'red', 'yellow', 'green']
    i = 0
    for key in descending_order.keys():
        plt.plot(powersizes, descending_order[key][1], color=colors[i], label=key)
        i += 1

    plt.title("Descending-ordered array")
    plt.yscale('log')
    plt.ylabel('Y : Time (in nanoseconds) (logarithmic scale)')
    plt.xlabel('X : Powersizes')
    plt.legend()
    plt.show()


def similar_values_comparisons():
    colors = ['blue', 'red', 'yellow', 'green']
    i = 0
    for key in similar_values.keys():
        plt.plot(powersizes, similar_values[key][0], color=colors[i], label=key)
        i += 1

    plt.title("Similar values array")
    plt.yscale('log')
    plt.ylabel('Y :Number of comparisons (logarithmic scale)')
    plt.xlabel('X : Powersizes')
    plt.legend()

    plt.show()


def similar_values_time():
    colors = ['blue', 'red', 'yellow', 'green']
    i = 0
    for key in similar_values.keys():
        plt.plot(powersizes, similar_values[key][1], color=colors[i], label=key)
        i += 1

    plt.title("Similar values array")
    plt.yscale('log')
    plt.ylabel('Y : Time (in nanoseconds) (logarithmic scale)')
    plt.xlabel('X : Powersizes')
    plt.legend()
    plt.show()

similar_values_time()