import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="#FFFFFF"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

    # Метод для зміни кольору вузла
    def set_color(self, color):
        self.color = color

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Реалізую DFS алгоритм
def dfs(node, depth=0):
    if node is not None:
        # Генерування кольору від темного до світлого для кожного вузла
        # Значення RGB збільшуються з кожним кроком, щоб забезпечити градієнт
        color_value = 255 - min(255, depth * 30) 
        hex_color = f"#{color_value:02x}{color_value:02x}ff"
        node.set_color(hex_color)
        
        # Рекурсивний обхід лівого піддерева
        dfs(node.left, depth + 1)
        # Рекурсивний обхід правого піддерева
        dfs(node.right, depth + 1)

dfs(root)

draw_tree(root)


# Реалізую BFS алгоритм
def bfs(root):
    queue = deque([(root, 0)]) 
    while queue:
        node, depth = queue.popleft()
        if node is not None:
            # Генерування кольору: кожен рівень має свій відтінок синього
            color_value = 255 - min(255, depth * 30)
            hex_color = f"#{color_value:02x}{color_value:02x}ff"
            node.set_color(hex_color)
            
            # Додавання дочірніх вузлів до черги
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))

# Скидаю кольори дерева до стандартних і виконуємо BFS
dfs(root)  # Скидання до початкових кольорів
bfs(root)  # Виконання BFS з зміною кольорів

draw_tree(root)

