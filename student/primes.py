def write_primes(n, path):
    '''
    Write primes under n to a specified file.
    :param n: int, The number to write primes under.
    :param path: str, The path to the file to write the primes to.
    :return: None
    '''
    # Delete the contents of the file if it already exists
    open(path, 'w').close()

    # Loop over all the possible prime numbers
    for i in range(2, n + 1):
        # Check if the number is prime
        if is_prime(i):
            #If it is prime, write it to the file
            with open(path, 'a') as file:
                file.write(str(i) + '\n')

def is_prime(n):
    '''
    Check if a number is prime.
    :param n: int, The number to check.
    :return: bool, True if the number is prime, False otherwise.
    '''

    # 0, 1, and negative numbers are not prime
    if n < 2:
        return False
    
    # Consider all numbers from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        # If a factor is found, the number is not prime
        if n % i == 0:
            return False
    # If no factors have been found, the number is prime
    return True