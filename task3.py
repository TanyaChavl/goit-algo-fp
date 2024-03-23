import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}
    
    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))
        
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append((u, weight))

    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0
        
        # Черга пріоритетів (бінарна купа), що зберігає вершини та їх поточні відстані
        # та ініціалізується початковою вершиною
        priority_queue = [(0, start)]
        
        while priority_queue:
            # Вибираю вершину з найменшою відстанню
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            # Якщо відстань у купі більша за вже знайдену, пропускаю ітерацію
            if current_distance > distances[current_vertex]:
                continue

            # Оновлюю відстані до сусідів поточної вершини
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                
                # Якщо знайдено коротший шлях, оновлюю відстань та додаю у купу
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
                    
        return distances

# Створення графу
graph = Graph(9)
edges = [
    (0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11), (2, 3, 7), 
    (2, 8, 2), (2, 5, 4), (3, 4, 9), (3, 5, 14), (4, 5, 10), 
    (5, 6, 2), (6, 7, 1), (6, 8, 6), (7, 8, 7)
]

# Додаю ребра до графа
for u, v, weight in edges:
    graph.add_edge(u, v, weight)

# Виконую алгоритм Дейкстри з початкової вершини 0
shortest_paths = graph.dijkstra(0)
print(f"Oбчислення найкоротших шляхів: {shortest_paths}")
