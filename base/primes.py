def write_primes(n, filename):
    open(filename, 'w').close()

    for i in range(2, n + 1):
        if is_prime(i):
            with open(filename, 'a') as file:
                file.write(str(i) + '\n')

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True