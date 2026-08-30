from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    count_characters_dict = {}

    for key in word:
        if key not in count_characters_dict:
            count_characters_dict[key] = 1
        elif key in count_characters_dict:
            count_characters_dict[key] += 1
    
    return count_characters_dict



# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
