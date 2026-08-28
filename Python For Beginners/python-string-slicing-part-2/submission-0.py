def first_n_characters(s: str, n: int) -> str:
    return(s[:n])

def last_n_characters(s: str, n: int) -> str:
    ending_index = len(s)
    starting_index = ending_index - n
    return(s[starting_index:ending_index])


# do not modify below this line
print(first_n_characters("NeetCode", 3))
print(first_n_characters("NeetCode", 4))
print(first_n_characters("NeetCode", 8))

print(last_n_characters("NeetCode", 3))
print(last_n_characters("NeetCode", 4))
print(last_n_characters("NeetCode", 8))
