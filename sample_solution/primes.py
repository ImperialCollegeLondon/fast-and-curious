

def write_primes(n, filename):
    primes = get_primes_under_n(n)

    with open(filename, 'w') as file:
        file.write('\n'.join(map(str, primes)))

def get_primes_under_n(n):
    primes = []
    for i in range(2, n + 1):
        for potential_factor in primes:
            if i % potential_factor == 0:
                break
        else:
            primes.append(i)

    return primes   

write_primes(100, 'primes.txt')