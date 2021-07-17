def my_function():
  print('I´m a function')

def outer_function():
  def inner_function():
    print('I came from the inner function.')
  # Executing the inner function inside the outer function.
  inner_function()

def second_outer_funtion():
  '''Assign task to student'''
  task = 'Read Python book chapter 3.'
  def inner_funtion():
    print(task)
  return inner_funtion()


def friendly_reminder(fn):
  '''Reminder for husband'''
  fn()
  print('Don\'t forget to bring your wallet!')

def action():
  print('I am going to the store buy you something nice.')


if __name__ == '__main__':
  print('Test one: simple function assignment to a variable')
  description = my_function
  print(description())

  print('Test two: nested function')
  outer_function()
  
  print('Test three: return nested function')
  homework = second_outer_funtion()

  print('Test four: function passed to another function as an argument')
  # Calling the friendly_reminder function with the action function used as an argument.
  friendly_reminder(action)