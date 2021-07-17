def pi_val():
  import math
  print(f'The value of PI is approximately {math.pi:.6f}')

def format_table_values():
  table = {
    'Sjoerd': 4127,
    'Jack': 4098,
    'Dcab': 7678,
  }
  for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')


if __name__ == '__main__':
  pi_val()
  format_table_values()