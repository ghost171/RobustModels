import heapq

import collections

#implementing dijkstra algorithm
def network_bandwidth(times: list[list[int]], n: int, x: int) -> int:
    adjacency_list = collections.defaultdict(list)

    for u, v, w in times:
        adjacency_list[u].append((v, w))

    heap_for_neighbours = [(0, x)] #starting point with distance 0 (because it's startinf point)
    visited = set()
    min_distance = 0
    while heap_for_neighbours:
        w, v = heapq.heappop(heap_for_neighbours) #when we visited node we have to pop it from heap
        if v in visited:
            continue
        visited.add(v)
        min_distance = max(min_distance, w) # choose between current node's distance and past  node's distnce
        for v_neighbour, w_neighbour in adjacency_list[v]:
            if v_neighbour not in visited:
                sum_distance = w + w_neighbour
                heapq.heappush(heap_for_neighbours, (sum_distance, v_neighbour)) #after  summing bandwidth on the current node we need to visit neighbour nodes 
                                                                                 #if they are not been visited
    if len(visited) == n:
        return min_distance
    else:
        return -1


if __name__ == "__main__":
    print(network_bandwidth([[1, 2, 1]], 2, 2))
