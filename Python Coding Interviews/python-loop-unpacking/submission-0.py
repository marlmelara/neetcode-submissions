from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    highest_score = 0
    for key, value in scores:
        if value > highest_score:
            highest_score = value
            best_student = key
        else:
            continue

    return best_student

# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
