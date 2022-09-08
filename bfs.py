from typing import List

import networkx as nx
from webcolors import rgb_to_hex

from abstractClass import ABCClass
from collections import deque
import matplotlib.pyplot as plt


class BFS(ABCClass):
    def find_shortest_path(self, start, end) -> List:
        start_idx, end_idx = self.set_default(start, end)
        k = deque()
        k.append(start_idx)
        while len(k) != 0:
            node = k.popleft()
            for city_idx, distance in self.adj_matrix[node]:
                if self.dist[city_idx] > self.dist[node] + distance:
                    self.dist[city_idx] = self.dist[node] + distance
                    k.append(city_idx)
                    self.parent[city_idx] = node
                    self.G.add_edge(
                        self.idx_to_city[node],
                        self.idx_to_city[city_idx],
                        weight=distance,
                        color=rgb_to_hex((self.red_value, self.green_value, self.blue_value))
                    )
                    self.increment_color(1)
        path = self.build_path(end_idx)
        self.draw_graph(self.get_method())
        self.save_graph(self.get_method())
        return list(map(lambda x: self.idx_to_city[x], path))

    def get_method(self) -> str:
        return 'BFS'
