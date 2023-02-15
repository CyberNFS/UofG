import time
from collections import defaultdict
import math

# O( n log log n)
# Sieve Erotosthenes


def print_primes(n):
    # Initialize a boolean array of size n+1 to track prime numbers
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    # Loop through all numbers from 2 to n, marking multiples as non-prime
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    # Print all prime numbers that are still marked as prime in the array
    for i in range(2, n + 1):
        if primes[i]:
            print(i, end=' ')


def get_primes(n):
    # Initialize a boolean array of size n+1 to track prime numbers
    primes = [True] * (n + 1)

    # Set 0 and 1 to be non-prime
    primes[0] = primes[1] = False

    # Loop through all numbers from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        # If i is still marked as prime, mark all multiples of i as non-prime
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    # Create a list of prime numbers from the boolean array
    prime_list = [i for i in range(2, n + 1) if primes[i]]

    # Return the list of prime numbers
    return prime_list


assert get_primes(200)[5] == 13
assert len(get_primes(2000)) == 303
assert len(get_primes(20000)) == 2262
assert get_primes(20000)[-1] == 19997
assert get_primes(200000)[-2] == 199967


# Pythagorean triplet Brute-Force O(n^2)

def find_pythagorean_triplet(n):
    # Loop through all possible values of a from 1 to n
    for a in range(1, n + 1):
        # Loop through all possible values of b from a+1 to n
        for b in range(a + 1, n + 1):
            # Calculate the value of c
            c = n - a - b
            # Check if c is a positive integer and satisfies the Pythagorean theorem
            if c > 0 and c**2 == a**2 + b**2:
                # If a Pythagorean triplet is found, return a dictionary with the values of a, b, and c
                return {'a': a, 'b': b, 'c': c}
    # If no Pythagorean triplet is found, return None
    return None


# Quadratic formula implementation O(n)

def find_pythagorean_triplet(n):
    # Loop through all possible values of a from 1 to n
    for a in range(1, n):
        # Compute the value of b using the quadratic formula
        b = (n**2 - 2 * n * a) / (2 * n - 2 * a)
        # Check if float is mathematically equivalent (describable) to an integer.
        if b.is_integer():
            # Compute the value of c
            c = n - a - int(b)
            # Check if a, b, and c form a Pythagorean triplet
            if c**2 == a**2 + b**2:
                # If a Pythagorean triplet is found, return a dictionary with the values of a, b, and c
                return {'a': a, 'b': int(b), 'c': c}

    # If no Pythagorean triplet is found, return None
    return None


result = find_pythagorean_triplet(1000)
if result is not None:
    print(result)
else:
    print("No Pythagorean triplet found for n=1000.")

# Longest Collatz Sequence ––––––––––––––––––––––––––––––––––––––––––––– >
constant = 20_000_000

start_time = time.time()


def collatz_sequence(n, memo):
    """Use memoization to avoid recomputing the length of the chain for
    previously seen values. Takes 'n' and a dict 'memo' as inputs, and
    returns the length of the chain for the value of 'n'."""
    if n == 1:
        return 1
    elif n in memo:
        return memo[n]
    elif n % 2 == 0:
        length = collatz_sequence(n // 2, memo) + 1
    else:
        length = collatz_sequence(3 * n + 1, memo) + 1
    memo[n] = length
    return length


def longest_chain(n):
    """Takes 'n' integer and returns a tuple = '(max_start, max_length)'
    representing = ('starting value','longest length up to n')."""

    # initialise to zero
    max_length = 0
    max_start = 0

    # empty dict to store the length of the sequences for each value 'n'
    memo = {}

    # Iterate over all starting values from 1 to n
    for start in range(1, n + 1):
        length = collatz_sequence(start, memo)

        # If the current length is greater than the maximum length seen so far,
        # update the maximum length and starting value.
        if length > max_length:
            max_length = length
            max_start = start

    # Return the starting value and chain length of the longest chain
    return (max_start, max_length)


print(longest_chain(constant))
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Memoisation: {elapsed_time:.12f}")
start_time = time.time()


def longest_chain(n):

    max_length = 0
    max_start = 0

    # Iterate over all starting values from 1 to n-1
    for start in range(1, n):
        length = 1
        num = start

        # Apply the Collatz sequence until the number reaches 1
        while num != 1:
            if num % 2 == 0:
                num //= 2
            else:
                num = 3 * num + 1
            length += 1

        # Update the maximum length and starting value if the current chain is longer
        if length > max_length:
            max_length = length
            max_start = start

    # Return the starting value and chain length of the longest chain
    return (max_start, max_length)


# print(longest_chain(constant))

end_time = time.time()
elapsed_time = end_time - start_time

# print(f"Brute Force: {elapsed_time:.12f}")
start_time = time.time()


from collections import defaultdict
import math


def collatz_sequence(n, memo):
    """Use memoization to avoid recomputing the length of the chain for
    previously seen values. Takes 'n' and a dict 'memo' as inputs, and
    returns the length of the chain for the value of 'n'."""
    if n == 1:
        return 1
    elif n in memo:
        return memo[n]
    elif n % 2 == 0:
        length = collatz_sequence(n // 2, memo) + 1
    else:
        length = collatz_sequence(3 * n + 1, memo) + 1
    memo[n] = length
    return length


def longest_chain(n):
    """Takes 'n' integer and returns a tuple = '(max_start, max_length)'
    representing = ('starting value','longest length up to n')."""

    # initialise to zero
    max_length = 0
    max_start = 0
    # empty dict to store the length of the sequences for each value 'n'
    memo = defaultdict(int)

    """ Log2(n) – yields the number of 'times 2' used to get 'n'
    Log2(Log2(n)) – number of times we can take 'log2(n)' before reaching one.
    Also called 'Mahler's conjecture' (Kurt Mahler)."""
    upper_bound = int(math.log2(n)) + int(math.log2(math.log2(n))) + 1

    # Iterate over all starting values from 1 to n
    for start in range(1, n + 1):
        length = collatz_sequence(start, memo)

        """ Multiple 'if' runs each condition-blocks and performs the
        associated action.

        If the current length is greater than the maximum length seen so far,
        update the maximum length and starting value."""
        if length > max_length:
            max_length = length
            max_start = start

        """If the length of the chain for the current value of start is less than or equal to
        the maximum length of the chain for values greater than start, we can skip the rest
        of the loop for values greater than start."""
        if length <= upper_bound:
            continue

        """Update the maximum length of the chain for values greater than start based on the
        length of the chain for the nearest odd number that has already been seen in the loop."""
        for i in range(start + 2, n + 1, 2):
            if collatz_sequence(i, memo) > length:
                upper_bound = collatz_sequence(i, memo)
                break

    # Return the starting value and chain length of the longest chain
    return (max_start, max_length)


print(longest_chain(constant))

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Kurt Mahler: {elapsed_time:.12f}")
