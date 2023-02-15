import multiprocessing
import sys


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


def longest_chain_parallel(start, end):
    # Create a pool of worker processes
    pool = multiprocessing.Pool()

    # Define a worker function to compute the chain length for a range of values
    def worker(start, end):
        memo = {}
        max_start = 0
        max_length = 0
        for n in range(start, end):
            length = collatz_sequence(n, memo)
            if length > max_length:
                max_length = length
                max_start = n
        return (max_start, max_length)

    # Split the range of values into chunks and assign them to the worker processes
    num_processes = multiprocessing.cpu_count()
    chunk_size = (end - start) // num_processes
    chunks = [(start + i * chunk_size, start + (i + 1) * chunk_size)
              for i in range(num_processes)]
    results = pool.starmap(worker, chunks)

    # Combine the results and return the longest chain
    max_start, max_length = max(results, key=lambda x: x[1])
    return (max_start, max_length)


print(longest_chain_parallel(sys.argv[1:2]))
