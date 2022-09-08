from typing import List, Dict
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    adj_matrix: List[List]
    G: nx.Graph

    def __init__(self, adj_matrix: List[List]):
        self.adj_matrix = adj_matrix.copy()
        self.G = nx.Graph()

    def create_graph(self, idx_to_city: Dict):
        for i in range(len(self.adj_matrix)):
            for city, distance in self.adj_matrix[i]:
                self.G.add_edge(idx_to_city[i], idx_to_city[city], weight=distance)

    def draw_graph(self):
        nx.draw_circular(self.G,
                node_color='cyan',
                node_size=500,
                with_labels=True)
        plt.show()
