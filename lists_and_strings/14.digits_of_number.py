def digits_of_number(number):
    result = []
    while number > 0 :
        digit = number % 10
        number = number // 10
        result.insert(0, digit)
    return result

print digits_of_number(1234)
