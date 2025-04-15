# Problem: https://www.hackerrank.com/challenges/queue-using-two-stacks/problem

import logging
from enum import Enum
from typing import Optional, Tuple

# Configure the logging format
logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class Command(Enum):
    ENQUEUE = 1
    DEQUEUE = 2
    PRINT = 3


class Stack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return f"Stack data: {self._data}"

    def push(self, value: int):
        self._data.append(value)

    def pop(self):
        return self._data.pop()

    def top(self) -> Optional[int]:
        if self._data:
            return self._data[-1]
        logging.warning(f"data: {self._data}")
        return None


class Queue:
    def __init__(self):
        self._head = Stack()
        self._tail = Stack()

    def enqueue(self, value: int):
        self._tail.push(value)

    def dequeue(self):
        logging.debug(f"head: {self._head}")
        if self._head:
            return self._head.pop()
        self._swap_tail_to_head()
        return self._head.pop()

    def peek(self) -> Optional[int]:
        if self._head:
            return self._head.top()
        self._swap_tail_to_head()
        return self._head.top()

    def _swap_tail_to_head(self):
        while self._tail:
            self._head.push(self._tail.pop())
        return


def read_command() -> Tuple[Command, Optional[int]]:
    instruction = input().strip().split(" ")
    cmd = int(instruction[0])
    if len(instruction) == 1:
        return Command(cmd), None
    try:
        arg = int(instruction[1])
    except ValueError:
        arg = instruction[1]
    return Command(cmd), arg


def main():
    q = Queue()
    n_commands = int(input().strip())

    for _ in range(n_commands):
        cmd, arg = read_command()
        if cmd == Command.ENQUEUE:
            q.enqueue(arg)
        if cmd == Command.DEQUEUE:
            q.dequeue()
        if cmd == Command.PRINT:
            print(q.peek())


# Tests' driver
if __name__ == "__main__":
    main()

"""
Input (stdin)
10
1 42
2
1 14
3
1 28
3
1 60
1 78
2
2
"""
