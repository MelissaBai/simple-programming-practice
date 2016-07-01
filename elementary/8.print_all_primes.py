def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


def print_primes(num):
    prime_list = []
    for i in range(num+1):
        if is_prime(i):
            prime_list.append(i)
    print(','.join(map(str, prime_list)))
    #print(final)

print_primes(24)
