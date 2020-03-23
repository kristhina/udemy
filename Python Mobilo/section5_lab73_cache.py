import functools
import time


@functools.lru_cache(maxsize=100)
def fib(n):
    if n <= 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result


for i in range(40):
    start_time = time.time()
    print(fib(i))
    stop_time = time.time()
    print("wartość:", i, "czas:", stop_time - start_time)
