from typing import List

from webcolors import rgb_to_hex

from abstractClass import ABCClass


class DFS(ABCClass):
    def find_shortest_path(self, start, end):
        start_idx, end_idx = self.set_default(start, end)
        self.dfs(start_idx)
        path = self.build_path(end_idx)
        self.draw_graph()
        return list(map(lambda x: self.idx_to_city[x], path))

    def dfs(self, idx: int):
        for city_idx, distance in self.adj_matrix[idx]:
            if self.dist[city_idx] > distance + self.dist[idx]:
                self.dist[city_idx] = distance + self.dist[idx]
                self.parent[city_idx] = idx
                self.G.add_edge(
                    self.idx_to_city[idx],
                    self.idx_to_city[city_idx],
                    weight=distance,
                    color=rgb_to_hex((self.red_value, self.green_value, self.blue_value))
                )
                self.increment_color(1)
                self.dfs(city_idx)

    def get_method(self):
        return 'DFS'
