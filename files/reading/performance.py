import tracemalloc
from functools import wraps
from time import perf_counter


def measure_performance(func):
    '''Measure performance of a function'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Start trace of memory blocks used
        tracemalloc.start()

        # Start stopwatch/counter
        start_time = perf_counter()
        
        # Execute decorated function
        func(*args, **kwargs)
        
        # Get current and peak traced memory
        current, peak = tracemalloc.get_traced_memory()

        # Clear traces of memory blocks allocated by Python
        # tracemalloc.clear_traces()

        # Stop trace of memory blocks used
        tracemalloc.stop()
        
        # Stop stopwatch/counter
        end_time = perf_counter()

        # Display results
        print(f"\n{'':*^45}")
        print(f"Function {func.__name__}")
        print(f"Details: {func.__doc__}")
        print(
            f"Memory usage:\t\t {current / (1024 * 1024):,.6f} MB\n"
            f"Peak memory usage:\t {peak / (1024 * 1024):,.6f} MB"
        )
        print(f"Time elapsed is:\t {end_time - start_time:,.6f} seconds")
        print(f"{'':*^45}")

    return wrapper
