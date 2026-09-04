from typing import List, Tuple


def sum_3_integers(triplet: List[int]) -> int:
    x, y, z = triplet
    total = x + y + z

    return total

def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    width, height, depth = box_dimensions
    volume = width * height * depth

    return volume

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
