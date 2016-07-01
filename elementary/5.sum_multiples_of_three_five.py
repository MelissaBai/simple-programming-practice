n = int(input("Please input a number "))
print(sum(i for i in range(1, n+1) if i%3==0 or i%5==0))
