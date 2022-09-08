from abc import ABC, abstractmethod
from typing import List, Dict

import networkx as nx
from matplotlib import pyplot as plt


class ABCClass(ABC):
    adj_matrix: List[tuple]
    city_to_idx: Dict
    idx_to_city: Dict
    n: int
    G: nx.DiGraph
    dist: List
    parent: List
    red_value: int = 30
    blue_value: int = 30
    green_value: int = 30

    def __init__(self, adj_matrix: List, city_to_idx: Dict, idx_to_city: Dict):
        self.adj_matrix = adj_matrix.copy()
        self.city_to_idx = city_to_idx.copy()
        self.idx_to_city = idx_to_city
        self.n = len(city_to_idx)
        self.G = nx.DiGraph()

    def set_default(self, start, end):
        self.dist = [float('+inf') for _ in range(self.n)]
        self.parent = [-1 for _ in range(self.n)]
        start_idx = self.city_to_idx[start]
        end_idx = self.city_to_idx[end]
        self.dist[start_idx] = 0
        self.red_value = 30
        self.green_value = 30
        self.blue_value = 30
        return start_idx, end_idx

    def build_path(self, start_idx) -> List:
        path = []
        cur_city = start_idx
        while self.parent[cur_city] != -1:
            path.append(cur_city)
            cur_city = self.parent[cur_city]
        path.append(cur_city)
        return reversed(path)

    def increment_color(self, red_increment):
        self.red_value += red_increment if self.red_value < 255 else 0
        # self.green_value += 2 if self.red_value >= 255 and self.green_value < 155 else 0
        # self.blue_value += 2 if self.red_value >= 255 and self.green_value >= 155 and self.blue_value < 155 else 0

    def draw_graph(self, title):
        edges, colors = zip(*nx.get_edge_attributes(self.G, 'color').items())
        ax = plt.gca()
        ax.set_title(title)
        nx.draw_circular(
            self.G,
            edgelist=edges,
            edge_color=colors,
            node_color='cyan',
            node_size=500,
            with_labels=True,
            ax=ax
        )

    @staticmethod
    def save_graph(filename):
        plt.savefig('./graphs/{}'.format(filename))
        plt.close()

    @abstractmethod
    def find_shortest_path(self, start, end):
        pass

    @abstractmethod
    def get_method(self):
        pass
