def chunk_classifier(memory, block_size):
    if block_size > len(memory):
        return -1
    
    for i in range(len(memory) // block_size):
        memory[i * block_size: (i + 1) * block_size] = [i] * block_size
    
    remainder = len(memory) % block_size 

    if remainder <= block_size // 2:
        memory[len(memory) - remainder:] = ['-'] * remainder
    if remainder > block_size // 2:
        memory[len(memory) - remainder:] = ['+'] * remainder

memory = ['x', 'x', 'x', 'x', 'x', 'x', 'x']
size = 4

chunk_classifier(memory, size)
print(memory)
