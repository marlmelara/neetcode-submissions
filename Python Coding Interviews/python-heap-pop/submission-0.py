import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    pop_order = []

    for i in range(len(heap)):
        if len(heap) != 0:
            pop_order.append(heap[0])
        
        heapq.heappop(heap)

    return pop_order

# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
