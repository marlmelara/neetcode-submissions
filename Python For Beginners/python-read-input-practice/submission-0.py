def add_two_numbers() -> int:
    user_input = input()
    string_list = user_input.split(',')
    int_list = [int(x) for x in string_list]
    two_sum = 0

    for i in int_list:
        two_sum += i

    return two_sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
