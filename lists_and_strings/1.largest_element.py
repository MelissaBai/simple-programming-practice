def largest_element(alist):
    n = alist[0]
    for e in alist:
        if e > n:
            n = e
    print(n)
    return(n)

largest_element([3,1,6,10,4,12])
