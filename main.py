import time
import itertools


def tsp(graph, start):
    n = len(graph)
    all_nodes = set(range(n))
    all_paths = []

    def backtrack(curr_node, visited, path, cost):
        visited.add(curr_node)
        path.append(curr_node)

        if len(visited) == n:
            all_paths.append((path + [start], cost + graph[curr_node][start]))
        else:
            for next_node in all_nodes - visited:
                backtrack(next_node, visited.copy(), path.copy(), cost + graph[curr_node][next_node])

        visited.remove(curr_node)
        path.pop()

    backtrack(start, set(), [], 0)

    all_paths.sort(key=lambda x: x[1])
    shortest_path = all_paths[0]

    return shortest_path


def print_iterations(paths, iterations=5):
    print("Iterasi Pertama:")
    for node in paths[0][0]:
        print(node, end=" ")
    print("\n")

    print("Iterasi Terakhir:")
    for node in paths[-1][0]:
        print(node, end=" ")
    print("\n")


def print_analysis():
    print("Worst Case: Algoritma TSP memiliki kompleksitas waktu O(n!).")
    print("Best Case: Tidak ada. Algoritma TSP memerlukan pencarian di semua kemungkinan rute.")
    print(
        "Average Case: Algoritma TSP memiliki kompleksitas waktu yang sangat tinggi dan sulit untuk ditentukan secara pasti.\n")


def main():
    graph = [
        [0, 2, 9, 10],
        [1, 0, 6, 4],
        [15, 7, 0, 8],
        [6, 3, 12, 0]
    ]
    start = 0

    print("Grafik:")
    for row in graph:
        print(row)
    print("\n")

    print("Perhitungan jalur terpendek dengan algoritma TSP...\n")

    start_time = time.time()
    shortest_path = tsp(graph, start)
    end_time = time.time()

    print("Hasil Akhir (Jalur Terpendek):")
    for node in shortest_path[0]:
        print(node, end=" ")
    print("\n")

    print("Waktu Komputasi Perhitungan Path:", end_time - start_time, "detik\n")

    print_iterations(shortest_path[0])

    print_analysis()


if __name__ == "__main__":
    main()
