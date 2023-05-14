import sys
import matplotlib.pyplot as plt
import random
import numpy as np
import scipy.interpolate

def build_line_charts(num_charts, name_of_y, num_of_lines, line_labels, chart_labels, *args):
    fig, axs = plt.subplots(1, num_charts, figsize=(15,5))
    for i, ax in enumerate(axs):
        for j in range(num_of_lines):
            x = np.linspace(0, len(args[i*num_of_lines + j])-1, 30)
            y = scipy.interpolate.interp1d(np.arange(len(args[i*num_of_lines + j])), args[i*num_of_lines + j], kind='cubic')(x)
            ax.plot(x, y, label=line_labels[j])
        x = np.linspace(0, len(args[i * num_of_lines]) - 1, 30)
        y = 0.5 * x * np.log(x)
        ax.plot(x, y, label='2*n*log(n)')
        y = x ** 2
        ax.plot(x, y, label='1/2*n^2')
        ax.set_title('Line Chart {}'.format(chart_labels[i]))
        ax.set_xlabel('n of elements')
        ax.set_ylabel(name_of_y)
        ax.legend()
    plt.tight_layout()
    plt.show()

def build_line_charts1(num_charts, name_of_y, num_of_lines, line_labels, chart_labels, *args):
    fig, axs = plt.subplots(1, num_charts, figsize=(15,5))
    for i, ax in enumerate(axs):
        for j in range(num_of_lines):
            x = np.linspace(0, len(args[i*num_of_lines + j])-1, 10)
            y = scipy.interpolate.interp1d(np.arange(len(args[i*num_of_lines + j])), args[i*num_of_lines + j], kind='cubic')(x)
            ax.plot(x, y, label=line_labels[j])
        ax.set_title('Line Chart {}'.format(chart_labels[i]))
        ax.set_xlabel('n of elements')
        ax.set_ylabel(name_of_y)
        ax.legend()
    plt.tight_layout()
    plt.show()
def measuring_operations(size, sort, arr_r):
    y_best = []
    y_worst = []
    y_random = []
    arr_a = create_ascending_array(size)
    arr_d = create_descending_array(size)

    for i in range(1, size+1):
        _, operations, swaps1 = sort(arr_a[:i])
        y_best.append(operations+swaps1)
        _, operations2, swaps2 = sort(arr_d[:i])
        y_worst.append(operations2+swaps2)
        _, operations3, swaps3 = sort(arr_r[:i])
        y_random.append(operations3+swaps3)
    return y_best, y_worst, y_random


def view(array):
    for i in range(len(array)):
        if not i % 10 == 0:
            print(array[i], end=' ')
        else:
            print('')
    print('\n')

def create_ascending_array(size):
    arr = list(range(1, size + 1))
   # print("arr_a before:")
    #view(arr)
    return arr


def create_descending_array(size):
    arr = list(range(size, 0, -1))
   # print("arr_d before:")
  #  view(arr)
    return arr


def create_random_array(size):
    arr = list(range(size))
    random.shuffle(arr)
  #  print("arr_r before:")
   # view(arr)
    return arr