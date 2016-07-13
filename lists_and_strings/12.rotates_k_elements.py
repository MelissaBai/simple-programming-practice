def rotates_by_k_elements(alist, k):
    if k > len(alist) and len(alist) != 0:
        k = k % len(alist)
    return alist[k:] + alist[:k]

test_cases = [
    (([1, 2, 3, 4, 5, 6], 3), [4, 5, 6, 1, 2, 3]),
    (([], 3), []),
    (([5], 3), [5]),
    (([1, 2, 3, 4, 5, 6], 1), [2, 3, 4, 5, 6, 1]),
    (([1, 2, 3, 4, 5, 6], 6), [1, 2, 3, 4, 5, 6]),
    (([1, 2, 3, 4, 5, 6], 7), [2, 3, 4, 5, 6, 1]),
    (([1, 2, 3, 4, 5, 6], 13), [2, 3, 4, 5, 6, 1]),
]

for args, expected in test_cases:
    assert rotates_by_k_elements(*args) == expected
    print(rotates_by_k_elements(*args))
