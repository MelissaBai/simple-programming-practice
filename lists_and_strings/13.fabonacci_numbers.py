def fibonacci_100():
    result = []
    result.insert(0, 1)
    result.insert(1, 1)
    for i in range(2,100):
        result.append(result[i-1] + result[i-2])
    return result
print fibonacci_100()



'''
Is there anything to improve for the script?
'''
