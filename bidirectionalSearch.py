from collections import deque

from webcolors import rgb_to_hex

from abstractClass import ABCClass


class BidirectionalSearch(ABCClass):
    def find_shortest_path(self, start, end):
        self.used = [0 for _ in range(self.n)]
        start_idx, end_idx = self.set_default(start, end)
        k = deque()
        k.append((start_idx, False))
        k.append((end_idx, True))
        flag = False
        while len(k) != 0 and not flag:
            node, is_reversed = k.popleft()
            self.increment_iter_cnt()
            for city_idx, distance in self.adj_matrix[node]:
                if not self.used[city_idx]:
                    self.used[city_idx] = 1 if is_reversed else 2
                    self.dist[city_idx] = self.dist[node] + distance
                    k.append((city_idx, is_reversed))
                    self.G.add_edge(
                        self.idx_to_city[node],
                        self.idx_to_city[city_idx],
                        weight=distance,
                        color=rgb_to_hex((self.red_value, self.green_value, self.blue_value))
                    )
                    self.increment_color(1)
                if self.used[city_idx] == (2 if is_reversed else 1):
                    self.G.add_edge(
                        self.idx_to_city[node],
                        self.idx_to_city[city_idx],
                        weight=distance,
                        color=rgb_to_hex((self.red_value, self.green_value, self.blue_value))
                    )
                    self.increment_color(1)
                    flag = True
                    break
        self.draw_graph(self.get_method())
        self.save_graph(self.get_method())
        print('{}: {}'.format(self.get_method(), self.iteration_counter))
        return ''

    def get_method(self):
        return 'Bidirectional search'
