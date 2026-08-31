from typing import List

def read_integers() -> List[int]:
    user_input = input()
    string_list = user_input.split(',')
    int_list = [int(i) for i in string_list]

    return int_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
