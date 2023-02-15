from collections import defaultdict
import math
import time
import sys

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


print(longest_chain(int(sys.argv[1])))

end_time = time.time()
elapsed_time = end_time - start_time

print(f"It took: {elapsed_time:.12f} seconds")
