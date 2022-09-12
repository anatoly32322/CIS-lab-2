from typing import List

from webcolors import rgb_to_hex

from abstractClass import ABCClass


class DFS(ABCClass):
    def find_shortest_path(self, start, end):
        start_idx, end_idx = self.set_default(start, end)
        self.dfs(start_idx)
        path = self.build_path(end_idx)
        self.draw_graph(self.get_method())
        self.save_graph(self.get_method())
        print('{}: {}'.format(self.get_method(), self.iteration_counter))
        return list(map(lambda x: self.idx_to_city[x], path))

    def dfs(self, node: int):
        self.increment_iter_cnt()
        for city_idx, distance in self.adj_matrix[node]:
            if self.dist[city_idx] > distance + self.dist[node]:
                self.dist[city_idx] = distance + self.dist[node]
                self.parent[city_idx] = node
                self.G.add_edge(
                    self.idx_to_city[node],
                    self.idx_to_city[city_idx],
                    weight=distance,
                    color=rgb_to_hex((self.red_value, self.green_value, self.blue_value))
                )
                self.increment_color(1)
                self.dfs(city_idx)

    def get_method(self):
        return 'DFS'
