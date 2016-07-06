def odd_position_element(alist):
    odd_elements = []
    for i in range(len(alist)):
        if i % 2 == 0:
            odd_elements.append(alist[i])
    print odd_elements
    return odd_elements


odd_position_element([1,4,7,2,8,4,2])


def slice(alist):
    print alist[::2]

slice([1,4,7,2,8,4,2])
