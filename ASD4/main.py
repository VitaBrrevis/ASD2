import random
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def graphix (graph):
    G = nx.DiGraph(np.matrix(graph))
    nx.draw(G, with_labels=True, node_size=300, arrows=False)
    plt.show()
def graph_validate(graph):
    for row in graph:
        if sum(row) % 2 != 0 or sum(row) == 0 :
            return False
    return True
def generate_random_graph(n):

    graph = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if random.choice([True, False]):
                graph[i][j] = 1
                graph[j][i] = 1

    for i in range(n):
        if sum(graph[i]) % 2 != 0:
            j = random.randrange(n)
            while i == j or graph[i][j] == 1:
                j = random.randrange(n)
            graph[i][j] = 1
            graph[j][i] = 1

    return graph
def print_graph(graph):
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
        print_graph(graph)
    else:
        print("Invalid input. Please enter 'M' or 'R'.\n")
        exit()

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
    graph = [[0, 1, 1, 1, 1],
             [1, 0, 0, 1, 0],
             [1, 0, 0, 1, 0],
             [1, 1, 1, 0, 1],
             [1, 0, 0, 1, 0]]
             """
    if graph_validate(graph):
        graphix(graph)
        cycle = fleury_algorithm(graph)
        print("Eulerian cycle:", ' -> '.join(str(x) for x in cycle))
    else:
        print("\nThe graph didn't pass the validation:\n there is either isolated nodes or\n the number of connections of some nodes are not even")
