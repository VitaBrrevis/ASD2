import random
import copy
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import networkx as nx
from itertools import combinations
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation

def animate_eulerian_cycle_and_graph(graph, cycle):
    # Создаем граф из матрицы смежности
    G = nx.Graph()
    n = len(graph)
    G.add_nodes_from(range(n))
    for i in range(n):
        for j in range(i+1, n):
            if graph[i][j] == 1:
                G.add_edge(i, j)

    # Задаем параметры графиков
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.set_title('Adjacency matrix')
    ax2.set_title('Graph')
    ax2.axis('off')
    pos = nx.spring_layout(G)

    # Рисуем граф из матрицы смежности
    G2 = nx.DiGraph(np.matrix(graph))
    nx.draw(G2, with_labels=True, node_size=300, arrows=False, ax=ax1)

    # Рисуем весь граф без ребер и с черными вершинами
    nx.draw_networkx(G, pos, node_color='black', edge_color='black', ax=ax2)

    # Функция анимации
    def animate(i):
        # Отрисовываем путь
        if i > 0:
            nx.draw_networkx_edges(G, pos, edgelist=[(cycle[i-1], cycle[i])], edge_color='green', width=2.0, ax=ax2)
            nx.draw_networkx_nodes(G, pos, nodelist=cycle[:i+1], node_color='green', node_size=500, ax=ax2)

        # Устанавливаем заголовок
        ax1.set_title("Step " + str(i+1))

    # Создаем анимацию
    ani = FuncAnimation(fig, animate, frames=len(cycle), interval=1000, repeat=False)

    # Отображаем графики
    plt.show()
def animate_eulerian_cycle(graph, cycle):
    # Создаем граф из матрицы смежности
    G = nx.Graph()
    n = len(graph)
    G.add_nodes_from(range(n))
    for i in range(n):
        for j in range(i+1, n):
            if graph[i][j] == 1:
                G.add_edge(i, j)

    # Задаем параметры графика
    fig, ax = plt.subplots()
    plt.axis('off')
    plt.title("Step 0")
    pos = nx.spring_layout(G)

    # Рисуем весь граф без ребер и с черными вершинами
    nx.draw_networkx(G, pos, node_color='black', edge_color='black')

    # Функция анимации
    def animate(i):
        # Отрисовываем путь
        if i > 0:
            nx.draw_networkx_edges(G, pos, edgelist=[(cycle[i-1], cycle[i])], edge_color='green', width=2.0)
            nx.draw_networkx_nodes(G, pos, nodelist=cycle[:i+1], node_color='green', node_size=500)

        # Устанавливаем заголовок
        plt.title("Step " + str(i+1))

    # Создаем анимацию
    ani = FuncAnimation(fig, animate, frames=len(cycle), interval=500, repeat=False)

    plt.show()
def graphix (graph):
    G = nx.DiGraph(np.matrix(graph))
    nx.draw(G, with_labels=True, node_size=300, arrows=False)
    plt.show()
def graph_validate(graph):
    n = len(graph)
    for row in graph:
        if sum(row) % 2 != 0 or sum(row) == 0:
            return False
    """""
    for i in range(n):
        diagonal_sum = 0
        for j in range(n):
            if (i + j) >= n:
                break
            else:
                diagonal_sum += abs(graph[n - (i + j) - 1][j])
        if diagonal_sum==0:
            return False
    
    for i in range(1, n):
        diagonal_sum = 0
        for j in range(n):
            if (i + j) >= n:
                break
            else:
                diagonal_sum += abs(graph[n - j - 1][i + j])
        if diagonal_sum == 0:
            return False
    """""
    diagonal_sum = 0
    for j in range(n):
        diagonal_sum+=graph[j][n-j-1]
    if diagonal_sum == 0:
        return False
    return True

import random

def generate_random_graph(n):
    random.seed()
    graph = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if random.choice([True, False]):
                graph[i][j] = 1
                graph[j][i] = 1

    for i in range(n):
        if sum(graph[i]) % 2 != 0:
            j = random.randrange(n)
            while i == j or graph[i][j] == 1 or sum(graph[j]) >= n-1:
                j = random.randrange(n)
            graph[i][j] = 1
            graph[j][i] = 1

    return graph

def print_graph(graph):
    print("the matrix analyzed:")
    n = len(graph)
    for i in range(n):
        for j in range(n):
            print(graph[i][j], end=" ")
        print()
def fleury_algorithm(graph):
    def index_s(line):
        index = -1
        for i in range(len(line)):
            if line[i] == 1:
                index = i
                return index
        return index
    def is_empty(graph):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if graph[i][j]!=0:
                    return False
        return True
    def standart(graph):
        nonlocal j
        while (not is_empty(graph)):
            index = index_s(graph[j])
            if index != -1:
                S.append(index)
                graph[j][index] = 0
                graph[index][j] = 0
                j = index
            else:
                C.append(S.pop())
                j = S[-1]
    C = []
    S = []
    j = 0
    S.append(0)
    standart(graph)
    while (len(S)!=0):
        C.append(S.pop())
    return C

if __name__ == '__main__':
    n = int(input("Enter number of vertices: "))
    option = input("Enter 'M' for manual input, or 'R' for random generation: ")
    if option.upper() == 'M':
        graph = []
        for i in range(n):
            row = list(map(int, input(f"Enter row {i+1} of adjacency matrix: ").split()))
            graph.append(row)
    elif option.upper() == 'R':
        graph = generate_random_graph(n)
        while (not graph_validate(graph)):
            graph = generate_random_graph(n)
        print_graph(graph)
    else:
        print("Invalid input. Please enter 'M' or 'R'.\n")
        exit()
    if graph_validate(graph):
        graph1 = copy.deepcopy(graph)
        cycle = fleury_algorithm(graph)
        print("Eulerian cycle:", ' -> '.join(str(x) for x in cycle))
        graphix(graph1)
        animate_eulerian_cycle(graph, cycle)

    else:
        print(
            "\nThe graph didn't pass the validation:\n there is either isolated nodes or\n the number of connections of some nodes are not even")

""""
    graph = [[0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
             [0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
             [0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
             [1, 0, 0, 1, 1, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 1, 1, 0, 1, 0, 0],
             [0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
             [0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
             [0, 0, 0, 1, 0, 0, 0, 0, 1, 0]]
"""
"""
    graph = [[0, 1, 1, 1, 1],
             [1, 0, 0, 1, 0],
             [1, 0, 0, 1, 0],
             [1, 1, 1, 0, 1],
             [1, 0, 0, 1, 0]]
"""
