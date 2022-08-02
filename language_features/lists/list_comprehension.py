def testing_list_comprehension():
  items = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
  filtered = [item * 2 for item in items if item % 2 == 0]
  print(f'Filtered: {filtered}')

if __name__ == '__main__':
  print(f'EXECUTING MAIN MODULE...')
  testing_list_comprehension()
  print(f'FINISHED!')