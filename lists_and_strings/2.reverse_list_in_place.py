def reverse_list(alist):
    length = len(alist)
    for i in range(length//2):
        n = alist[i]
        alist[i] = alist[-(i+1)]
        alist[-(i+1)] = n
    print (alist)




reverse_list([1,4,6,7,1,8])
