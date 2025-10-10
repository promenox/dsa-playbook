# sup learning materials
'''
https://youtu.be/2fA1FdxNqiE?si=Srfk4zwbYXW2-Jhg ~  Max Heapify w/ Complete Binary Tree | Ravindrababu Ravula
https://youtu.be/HI97KDV23Ig?si=HC0WwYdC0GaypUz4 ~ Build Max Heap | Ravindrababu Ravula
https://web.stanford.edu/class/archive/cs/cs161/cs161.1168/lecture4.pdf ~ Heaps | Stanford University
'''

# == heap notes ==

# height | 1  | 2  | 3  | 4  |  max on n-ary tree:
# max    | 3  | 7  | 15 | 31 |  (2^(h+1))-1

# log_{2} of n = tree height

# heapify O(n)

# -- min and max (will be @ root) --

# heap pop O(log_n)

# heap push O(log_n)

# heap peek O(1)

# -- alternative sorting algo --
# O(n log n)

class Heap:
    # initalize list of defined input nodes or []
    def __init__(self, input_nodes=None):
        # using list to make a new list not referenced by last input (safer)
        self.nodes = list(input_nodes) if input_nodes is not None else []

    # number of nodes in tree
    def __len__(self):
        return len(self.nodes)

    # -- binary tree nav --
    # left child idx: 2i+1
    def get_left_child_idx(self, parent_idx):
        return 2 * parent_idx +1

    # right child idx: 2i+2
    def get_right_child_idx(self, parent_idx):
        return 2 * parent_idx +2

    # parent inx: i//2
    # |: python arrays are 0 indexed so i - 1
    def get_parent_idx(self, child_idx):
        return (child_idx - 1) // 2 

    # leaf nodes index range [n//2] + 1, where n is heap size
    def get_leaf_nodes_start_idx(self):
        return self.get_heap_size() + 1
    
class MaxHeap(Heap):
    def __init__(self, input_nodes=None):
        super().__init__(input_nodes)
        self.build_max_heap()

    def build_max_heap(self):
        n = len(self.nodes)
        # ranges non inclusive so -1 stops 0
        for i in range(n//2, -1, -1):
            self.max_heapify(i)
    
    def max_heapify(self, idx):
        # heap size
        size = len(self.nodes)

        # child nodes
        left = self.get_left_child_idx(idx)
        right = self.get_right_child_idx(idx)

        # keeping track of largest node idx
        largest = idx

        # (left & right < size) ~ a check if child exists {because tree nodes indexed left to right in bin tree}
        # if child is larger it needs to be swapped
        if left < size and self.nodes[left] > self.nodes[largest]:
            largest = left # update idx to be left

        if right < size and self.nodes[right] > self.nodes[largest]:
            largest = right #update idx to be right

        # swap and recurse
        if largest != idx:
            self.nodes[idx], self.nodes[largest] = self.nodes[largest], self.nodes[idx]
            self.max_heapify(largest)

# implement a min heap setup ...

# jury-rigged test bed
arr = [3, 1, 2, 8]
max_heap = MaxHeap(arr)
print(max_heap.nodes)