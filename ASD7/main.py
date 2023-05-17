import sys
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def convert_to_bst(root):
    values = []
    in_order_traversal(root, values)
    values.sort()
    index = 0
    in_order_update(root, values, index)

def in_order_traversal(node, values):
    if node is None:
        return
    in_order_traversal(node.left, values)
    values.append(node.value)
    in_order_traversal(node.right, values)

def in_order_update(node, values, index):
    if node is None:
        return index
    index = in_order_update(node.left, values, index)
    node.value = values[index]
    index += 1
    index = in_order_update(node.right, values, index)
    return index


def find_paths(root, target_sum):
    paths = []
    current_path = []
    find_paths_recursive(root, target_sum, current_path, paths)
    return paths


def find_paths_recursive(node, target_sum, current_path, paths):
    if node is None:
        return
    current_path.append(node.value)
    find_paths_recursive(node.left, target_sum, current_path, paths)
    find_paths_recursive(node.right, target_sum, current_path, paths)
    current_sum = 0
    for i in range(len(current_path) - 1, -1, -1):
        current_sum += current_path[i]
        if current_sum == target_sum:
            paths.append(list(current_path[i:]))
    current_path.pop()


# Зчитування вхідних даних з файлу
def read_input(file_name):
    with open(file_name, 'r') as file:
        nodes = file.readline().strip().split()
        return nodes


# Запис результату у файл
def write_output(file_name, paths):
    with open(file_name, 'w') as file:
        for path in paths:
            file.write(' '.join(map(str, path)) + '\n')


# Основна функція
def main():
    import sys

    if len(sys.argv) < 3:
        print("Usage: python script.py input_file output_file")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    nodes = read_input(input_file)
    root = build_tree(nodes)
    convert_to_bst(root)
    target_sum = 9
    paths = find_paths(root, target_sum)
    write_output(output_file, paths)


# Допоміжна функція для побудови дерева зі списку ву
def build_tree(nodes):
    if not nodes:
        return None
    value = int(nodes.pop(0))
    if value == 0:
        return None
    node = Node(value)
    node.left = build_tree(nodes)
    node.right = build_tree(nodes)
    return node


input_file = sys.argv[1]
output_file = sys.argv[2]

nodes = read_input(input_file)
root = build_tree(nodes)
convert_to_bst(root)
target_sum = 513
paths = find_paths(root, target_sum)
write_output(output_file, paths)
