from tree import linked_list_tree as tree

from queue import Queue
from stack import Stack

# reconstructs the backtrace of the found solution
def reconstruct_path(parent, start, goal):
    path = [goal]
    node = goal

    while node != start:
        node = parent[node]
        path.append(node)

    return path[::-1]

# BFS search
def bfs_search(tree, start, goal):

    closed_set = []
    open_set = Queue([start])
    parent = {'S': None}

    while True:
        if (open_set.isEmpty()):
            break
        
        node = open_set.dequeue()
        closed_set.append(node)

        if node == 'G':
            break
        
        for child in tree[node]:
            parent[child] = node
            open_set.enqueue(child)

    return reconstruct_path(parent, start, goal)

print(bfs_search(tree, 'S', 'G'))

# DFS search

