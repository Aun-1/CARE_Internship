import numpy as np

class MemoryAllocator:
    def __init__(self, X, W, block_size):
        self.X = X
        self.W = W
        self.block_size = block_size
        self.mem_lists = {}
        self.initialize_mem_lists()

    def initialize_mem_lists(self):
        for i in range(self.block_size):
            list_name = f"mem{i}"
            self.mem_lists[list_name] = []

    def allocate_X(self):
        count = 0
        for i in range(self.X.shape[0]):
            list_name = f"mem{count}"
            self.mem_lists[list_name].append(self.X[i])
            count += 1
            if count == self.block_size:
                count = 0

    def allocate_W(self):
        count = 0
        for column in range(self.block_size, self.W.shape[1] + 1, self.block_size):
            for row in range(self.W.shape[0]):
                list_name = f"mem{count}"
                self.mem_lists[list_name].extend(self.W[row, column - self.block_size:column].tolist())
                count += 1
                if count == self.block_size:
                    count = 0

    def print_mem_lists(self):
        print(self.mem_lists)

# Example usage
X = np.array([1, 2, 3, 4])
W = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
bs = 4

allocator = MemoryAllocator(X, W, bs)
allocator.allocate_X()
allocator.allocate_W()
allocator.print_mem_lists()