import random
def fleury_algorithm(graph):

    g = [row[:] for row in graph]
    n = len(g)
    m = sum(len(row) for row in g) // 2
    cycle = [0]
    v = 0
    while len(cycle) < m + 1:
        edge_index = -1
        for i in range(len(g[v])):
            if g[v][i]:
                if edge_index == -1:
                    edge_index = i
                elif not is_bridge(g, v, i):
                    edge_index = i
                    break
        if edge_index == -1:
            break
        cycle = insert_edge(cycle, edge_index, v)
        g[v][edge_index] = g[edge_index][v] = 0
        v = cycle[edge_index]
        if v not in cycle:
            v = cycle[-1]
    return cycle


def insert_edge(cycle, edge_index, v):
    if edge_index + 1 == len(cycle):
        cycle.append(v)
    elif edge_index + 1 < len(cycle):
        cycle[edge_index + 1], cycle[edge_index] = cycle[edge_index], cycle[edge_index + 1]
    else:
        cycle.append(v)
    return cycle


def is_bridge(g, u, v):
    n = len(g)
    visited = [False] * n
    stack = [u]
    while stack:
        x = stack.pop()
        if not visited[x]:
            visited[x] = True
            for i in range(n):
                if g[x][i] and i != v and not (x == u and i == v):
                    stack.append(i)
    return not visited[v]

def graph_validate(graph):

    length = len(graph)
    one = False
    for i in range(length):

        # validation for isolation
        if not ( 1 in graph[i] ):
            one = True
            break

        # validation for even number of connections
        if sum(graph[i]) % 2:
            one = True
            break

    if one:
        return False
    return True



def generate_random_graph(n):
    graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if random.choice([True, False]):
                graph[i][j] = graph[j][i] = 1
    return graph

def is_eulerian(graph):
    n = len(graph)
    degree_sequence = [sum(graph[i]) for i in range(n)]
    return all(d % 2 == 0 for d in degree_sequence)

def dfs(node, visited, graph):
    visited[node] = True
    for i in range(len(graph[node])):
        if graph[node][i] and not visited[i]:
            dfs(i, visited, graph)

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
    else:
        print("Invalid input. Please enter 'M' or 'R'.\n")
        exit()

    if graph_validate(graph):
        cycle = fleury_algorithm(graph)
        print("Eulerian cycle:", ' -> '.join(str(x) for x in cycle))
    else:
        print("\nThe graph didn't pass the validation:\n there is either isolated nodes or\n the number of connections of some nodes are not even")

