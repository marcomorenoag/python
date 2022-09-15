import os
from enum import Enum
from types import FunctionType

from performance import measure_performance


class FileNames(Enum):
    DEFAULT = 'test_file.txt'


@measure_performance
def file_reader(file_name: str):
    '''Classic Pythonic way to read a file'''
    # file = open(file_name, 'r')
    # result = file.read().split('\n')
    # file.close()
    # return result
    with open(file_name, 'r') as file:
        for row in file.readlines():
            pass


@measure_performance
def file_reader_efficient(file_name: str):
    '''Pythonic way using generator'''
    for row in open(file_name, 'r'):
        yield row
    # Next lines (generator expression) are equivalent that above lines
    '''
    (row for row in open(file_name, 'r'))
    '''

# @measure_performance
def row_counting(file_reader: FunctionType) -> float:
    file_gen = file_reader
    row_count = 0

    for _ in file_gen:
        row_count += 1
    
    return row_count


def get_file_stats():
    print(f"{'File statistics':*^30}")
    file_stats = os.stat(FileNames.DEFAULT.value)
    print(f"File Size: {float(file_stats.st_size / (1024 * 1024)):,.2f} MB")


def counting_lines_performance():
    print(f"{'Counting file lines':*^30}")
    file_reader(FileNames.DEFAULT.value)
    file_reader_efficient(FileNames.DEFAULT.value)
    # row_counting(file_reader(FileNames.DEFAULT.value))
    # row_counting(file_reader_efficient(FileNames.DEFAULT.value))
    # row_counting((row for row in open(FileNames.DEFAULT.value, 'r')))


def main() -> None:
    get_file_stats()
    counting_lines_performance()


if __name__ == '__main__':
    main()
