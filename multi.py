
import sys
import numpy as np


def collatz_sequence(n):
    """Calculate the collatz sequence for the value of 'n' using NumPy vectorization.
    Returns the length of the chain for the value of 'n'."""
    memo = np.zeros(n + 1, dtype=np.int32)
    memo[1] = 1
    vals = np.arange(2, n + 1, dtype=np.int32)
    lengths = np.ones(n - 1, dtype=np.int32)
    i = 0
    while len(vals) > 0:
        lengths[vals % 2 == 0] += 1
        lengths[vals % 2 == 1] += memo[3 * vals[vals % 2 == 1] + 1] + 1
        memo[vals] = lengths
        vals = vals[vals != 1]
        lengths = lengths[vals != 1]
        i += 1
    return memo


def longest_chain(n):
    """Takes 'n' integer and returns a tuple = '(max_start, max_length)'
    representing = ('highest starting value','longest length up to n')."""

    # Initialise to zero
    max_length = 0
    max_start = 0

    # Calculate the collatz sequence lengths for all values from 1 to n
    sequence_lengths = collatz_sequence(n)

    # Find the starting value with the maximum sequence length
    max_start = np.argmax(sequence_lengths)
    max_length = sequence_lengths[max_start]

    # Return the starting value and chain length of the longest chain
    return (max_start, max_length)


print(longest_chain(sys.argv[1]))
