def sum_numbers_for(numbers):
    result = 0
    for item in numbers:
        result += item
    return result


def sum_numbers_while(numbers):
    result = 0
    i = 0
    while i < len(numbers):
        result += numbers[i]
        i += 1
    return result


def sum_numbers_recursive(numbers):
    result = 0
    if len(numbers) == 0:
        return 0
    elif len(numbers) == 1:
        return numbers[0]
    return numbers[0] + sum_numbers_recursive(numbers[1:])


print sum_numbers_for([1,2,3,4,5])
print sum_numbers_while([1,2,3,4,5])
print sum_numbers_recursive([1,2,3,4,5])
print sum_numbers_for([])
print sum_numbers_while([])
print sum_numbers_recursive([])
