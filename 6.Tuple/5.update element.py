original_list = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]
value_to_add = 4
updated_list = []
for tup in original_list:
    updated_tuple = []
    for element in tup:
        updated_element = element + value_to_add
        updated_tuple.append(updated_element)
    updated_list.append(tuple(updated_tuple))
print(updated_list)
