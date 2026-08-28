from typing import List

def contains_duplicate(words: List[str]) -> bool:
    my_set = set(words)
    unique_words = list(my_set)

    if len(words) != len(unique_words):
        return True
    else:
        return False

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
