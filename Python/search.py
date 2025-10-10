# import pandas as pd

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

# bfs search
def bfs_search(tree, start, goal):

    closed_set = []
    open_set = Queue([start])
    parent = {'S': None}

    idx = 0

    while True:
        
        print(f"idx:{idx}\nclosed:\t{closed_set}\nopen:\t{open_set.queue}\n")

        if (open_set.isEmpty()):
            break
        
        node = open_set.dequeue()
        closed_set.append(node)

        if node == 'G':
            break
        
        for child in tree[node]:
            parent[child] = node
            open_set.enqueue(child)
        
        idx += 1 

    
    return reconstruct_path(parent, start, goal)

# dfs search
def dfs_search(tree, start, goal):
    closed_set = []
    open_set = Stack([start])
    parent = {'S': None}

    idx = 0

    while True:
        
        print(f"idx:{idx}\nclosed:\t{closed_set}\nopen:\t{open_set.stack}\n")

        if (open_set.isEmpty()):
            break
        
        node = open_set.pop()
        closed_set.append(node)

        if node == 'G':
            break

        # we need to reverse the left of child nodes to get the l -> r convention
        for child in reversed(tree[node]):
            parent[child] = node
            open_set.push(child)
        
        idx += 1 
    
    return reconstruct_path(parent, start, goal)

print(bfs_search(tree, 'S', 'G'))
print(dfs_search(tree, 'S', 'G'))
