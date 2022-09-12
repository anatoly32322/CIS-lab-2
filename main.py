from bfs import BFS
from dfs import DFS
from dfsWithDepth import DFSWithDepth
from dfsIterativeDepth import DFSIterativeDepth
from bidirectionalSearch import BidirectionalSearch
from firstBestMatch import FirstBestMatch
from minimizingTotalScore import MinimizingTotalScore
import sys


METHODS = [
    BFS,
    DFS,
    DFSWithDepth,
    DFSIterativeDepth,
    BidirectionalSearch,
    FirstBestMatch,
    MinimizingTotalScore
]


def main(path):
    adj_matrix, city_to_idx_map, idx_to_city_map = read_file(path)
    for method in METHODS:
        solver = method(adj_matrix, city_to_idx_map, idx_to_city_map)
        solver.find_shortest_path('Вильнюс', 'Одесса')


def read_file(path):
    with open(path, encoding='utf-8') as f:
        city_array = list(f.readline().split())
        city_to_idx_map, idx_to_city_map = city_to_idx(city_array)
        adj_matrix = [[] for _ in range(len(city_to_idx_map))]
        for link in f:
            new_link = list(link.split())
            new_link[2] = int(new_link[2])
            adj_matrix[city_to_idx_map[new_link[0]]].append((
                city_to_idx_map[new_link[1]],
                new_link[2]
            ))
            adj_matrix[city_to_idx_map[new_link[1]]].append((
                city_to_idx_map[new_link[0]],
                new_link[2]
            ))
    return adj_matrix, city_to_idx_map, idx_to_city_map


def city_to_idx(city_array) -> dict:
    result_map = dict()
    reversed_result_map = dict()
    for idx, city in enumerate(city_array):
        result_map[city] = idx
        reversed_result_map[idx] = city
    return result_map, reversed_result_map


if __name__ == '__main__':
    main(sys.argv[1])
