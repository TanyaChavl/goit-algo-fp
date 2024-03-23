import uuid
import networkx as nx
import matplotlib.pyplot as plt
import math

class Node:
    def __init__(self, key, color="skyblue"):
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def insertKey(self, k):
        self.heap.append(Node(k))
        i = len(self.heap) - 1
        while i != 0 and self.heap[self.parent(i)].val > self.heap[i].val:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def drawHeap(self):
        if not self.heap:
            return

        tree = nx.DiGraph()
        pos = {}
        levels = math.ceil(math.log(len(self.heap) + 1, 2))
        for i in range(len(self.heap)):
            pos[self.heap[i].id] = (i, -int(math.log(i + 1, 2)))
            if i != 0:  # if not root
                parent_id = self.heap[self.parent(i)].id
                tree.add_edge(parent_id, self.heap[i].id)

        for node in self.heap:
            tree.add_node(node.id, color=node.color, label=node.val)

        colors = [node[1]['color'] for node in tree.nodes(data=True)]
        labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

        plt.figure(figsize=(8, 5))
        nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, node_shape="o")
        plt.show()

heap = MinHeap()
heap.insertKey(3)
heap.insertKey(2)
heap.insertKey(15)
heap.insertKey(5)
heap.insertKey(4)
heap.insertKey(45)

heap.drawHeap()
