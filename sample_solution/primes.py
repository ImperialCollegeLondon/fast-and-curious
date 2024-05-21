def write_primes(n, path):
    '''
    Write primes under n to a specified file.
    :param n: int, The number to write primes under.
    :param path: str, The path to the file to write the primes to.
    :return: None
    '''

    # Find all the primes under n
    primes = get_primes_under_n(n)

    # Write the primes to the file
    with open(path, 'w') as file:
        # The map function is used to convert all the primes to strings
        # The join function is used to concatenate all the primes into a single string
        # Each prime is separated by a newline character
        file.write('\n'.join(map(str, primes)))

def get_primes_under_n(n):
    '''
    Get all the primes under n (inclusive).
    :param n: int, The number to get primes under.
    :return: list, A list of all the primes under n.
    '''

    # There are no primes under 2
    if n < 2:
        return []
    
    # 2 is the only even prime
    primes = [2]
    # Consider all odd numbers from 3 to n
    for i in range(3, n + 1, 2):
        # Check if the number has any prime factors
        for potential_factor in primes:
            # If a prime factor is found, the number is not prime
            if i % potential_factor == 0:
                # Skip to the next number
                break
        else:
            # If no prime factors are found, the number is prime
            # Add it to the list of primes
            primes.append(i)

    # Return the final list of primes
    return primes   

