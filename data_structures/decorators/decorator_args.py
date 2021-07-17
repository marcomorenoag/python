# NOTE: Decorators hide the function they are decorating
# To avoid that we new to use below module
from functools import wraps

def my_decorator_func(func):
  '''*args will take an unlimited number of arguments of any type, such as 10, True, or 'Brandon'''
  '''**kwargs will take an unlimited number of keyword arguments, such as count=99, is_authenticated=True, or name='Brandon'''
  @wraps(func)
  def wrapper_fun(*args, **kwargs):
    # Do something before the function.
    func(*args, **kwargs)
    # Do something after the function
  return wrapper_fun

@my_decorator_func
def my_func(my_arg):
  '''Example docstring for function'''
  pass


if __name__ == '__main__':
  '''Decorators hide the function they are decorating. If I check the __name__ or __doc__ method we get an unexpected result.'''
  print(my_func.__name__)
  print(my_func.__doc__)
