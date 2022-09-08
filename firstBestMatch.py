from typing import List
from multipledispatch import dispatch
from collections import deque

from webcolors import rgb_to_hex

from abstractClass import ABCClass


class FirstBestMatch(ABCClass):
    pre_calc: List

    def find_shortest_path(self, start, end):
        start_idx, end_idx = self.set_default(start, end)
        self.pre_calculate_dist(start_idx)
        k = deque()
        k.append(end_idx)
        path = [end]
        while True:
            node = k.popleft()
            best_node = (node, self.dist[node])
            for city_idx, _ in self.adj_matrix[node]:
                if best_node[1] > self.dist[city_idx]:
                    best_node = (city_idx, self.dist[city_idx])
            if best_node[0] == node:
                break
            self.G.add_edge(
                self.idx_to_city[node],
                self.idx_to_city[best_node[0]],
                color=rgb_to_hex((self.red_value, self.green_value, self.blue_value))
            )
            self.increment_color(1)
            k.append(best_node[0])
            path.append(self.idx_to_city[best_node[0]])
        self.draw_graph(self.get_method())
        self.save_graph(self.get_method())
        return path

    def pre_calculate_dist(self, start_idx):
        k = deque()
        k.append(start_idx)
        while len(k) != 0:
            node = k.popleft()
            for city_idx, distance in self.adj_matrix[node]:
                if self.dist[city_idx] > self.dist[node] + distance:
                    self.dist[city_idx] = self.dist[node] + distance
                    k.append(city_idx)

    def get_pre_calculation(self, pre_calc):
        self.pre_calc = pre_calc.copy()

    def get_method(self):
        return 'First best match'
