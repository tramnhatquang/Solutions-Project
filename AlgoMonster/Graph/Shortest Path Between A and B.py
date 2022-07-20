from collections import deque
from typing import List


def shortest_path(graph: List[List[int]], a: int, b: int) -> int:
	# WRITE YOUR BRILLIANT CODE HERE

	# The problem is to find the shortest path between a and b we'll prefer
	# BFS in this problem than DFS since it is used to traverse all the
	# adjacent nodes of the current node before exploring further down the
	# paths

	# we use a deque() to illustrate the BFS. For each child of the root node,
	# we check if the child's value is equal to b, if not we append all the
	# neighbors of the child node into the deque We process all the nodes in
	# the same level before moving on to the next level. We also keep track of
	# the current distance from the root. In the next level, we increment the
	# distance by 1 We also use a visited set to keep track of all the visited
	# node, so that we do not check a node twice

	# time: O(n + m), n is the number of nodes, m is the number of edges
	# space: O(h)
	queue = deque([(a, 0)])
	visited = set()
	#     distance = 0
	while queue:
		n = len(queue)
		for _ in range(n):
			node, dist = queue.popleft()
			if node == b:
				return dist
			# append each child's node into the queue
			for child in graph[node]:
				if child in visited:
					continue
				visited.add(child)
				queue.append((child, dist + 1))


if __name__ == '__main__':
	graph = [[int(x) for x in input().split()] for _ in range(int(input()))]
	a = int(input())
	b = int(input())
	res = shortest_path(graph, a, b)
	print(res)
