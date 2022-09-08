from typing import List

from webcolors import rgb_to_hex

from abstractClass import ABCClass


class FirstBestMatch(ABCClass):
    used: List
    path: List = []
    flag: bool = False
    end_idx: int

    def find_shortest_path(self, start, end):
        self.used = [0 for _ in range(self.n)]
        start_idx, end_idx = self.set_default(start, end)
        self.end_idx = end_idx
        self.path.append((start, 0))
        self.first_best_match_dfs(start_idx)
        self.draw_graph(self.get_method())
        self.save_graph(self.get_method())
        return self.path

    def first_best_match_dfs(self, node):
        if self.flag:
            return
        if node == self.end_idx:
            self.flag = True
            return
        node_arr = []
        self.used[node] = 1
        for city_idx, distance in self.adj_matrix[node]:
            if not self.used[city_idx]:
                node_arr.append((city_idx, distance))
        node_arr.sort(key=lambda a: a[1])
        for city_idx, distance in node_arr:
            self.path.append((self.idx_to_city[city_idx], distance))
            self.G.add_edge(
                self.idx_to_city[node],
                self.idx_to_city[city_idx],
                color=rgb_to_hex((self.red_value, self.green_value, self.blue_value))
            )
            self.increment_color(10)
            self.first_best_match_dfs(city_idx)
            if self.flag:
                break
            self.path.pop()

    def get_method(self):
        return 'First best match'
