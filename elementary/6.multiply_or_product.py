import functools

def product(nums):
    return functools.reduce(lambda x, y: x * y, nums, 1)

def mysum(nums):
    return functools.reduce(lambda x, y: x + y, nums, 0)

def main():
    n = int(input("Please input a number. "))
    choice = input("Do you want the sum or product of 1 to n? Enter S or P. ")
    nums = range(1, n+1)
    if choice.upper() == 'S':
        print(mysum(nums))
    elif choice.upper() == 'P':
        print(product(nums))
    else:
        print("You didn't follow the instructions!")
        main()

main()

def sum_or_prod():
    choice = input("Do you want to sum or product of 1 to n? Press S or P. ")
    if choice.upper() == "S":
        sum = 0
        for i in range(1,n+1):
            sum += i
        print(sum)
    elif choice.upper() == "P":
        product = 1
        for i in range(1, n+1):
            product *= i
        print(product)
    else:
        print ("Please only type S or P")
        sum_or_prod()


'''
questions:
1. line 16, why can't it be if else?
2. Why do sum and product have to be defined at the beginning instead
of right after if statement.
'''
