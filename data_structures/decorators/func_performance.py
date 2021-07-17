from functools import wraps
import tracemalloc
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
    # Stop stopwatch/counter
    finish_time = perf_counter()
    # Display results
    print(f'Function: {func.__name__}')
    print(f'Method: {func.__doc__}')
    print(
      f'Memory usage:\t\t {current / 10**6:.6f} MB\n'
      f'Peak memory usage:\t {peak / 10**6:.6f} MB'
    )
    print(f'Time elapsed is:\t {finish_time - start_time:.6f} seconds')
    print(f'{"-"*45}')
    # Stop trace of memory blocks used
    tracemalloc.stop()
  return wrapper


# Unit testing
if __name__ == '__main__':
  @measure_performance
  def make_list1():
    '''Range'''
    my_list = list(range(100_000))

  @measure_performance
  def make_list2():
    '''List Comprehension'''
    my_list = [item for item in range(100_000)]

  @measure_performance
  def make_list3():
    '''Append'''
    my_list = []
    for item in range(100_000):
      my_list.append(item)

  @measure_performance
  def make_list4():
    '''Concatenation'''
    my_list = []
    for item in range(100_000):
      my_list = my_list + [item]

  print(make_list1())    
  print(make_list2())
  print(make_list3())
  print(make_list4())