def combine_lists_alternatively(lista, listb):
    result = []
    for a, b in zip(lista, listb):
        result.extend([a, b])
    return result
print combine_lists_alternatively([1,2,3], ['a', 'b', 'c', 'd'])
