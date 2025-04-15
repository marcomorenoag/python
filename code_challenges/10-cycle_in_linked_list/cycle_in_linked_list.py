# Problem: https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def has_cycle(head):
    """
    Second solution: 2 pointer (1 slow & 1 fast), aka Tortoise and Hare
    Time  => O(n)
    Space => O(1)
    """
    slow_ptr = head
    fast_ptr = head.next
    while fast_ptr is not None and fast_ptr.next is not None:
        if slow_ptr == fast_ptr:
            return 1
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    return 0


def init_has_cycle(head):
    """
    First solution: keep tracking of visited nodes
    Time  => O(n)
    Space => O(n)
    """
    seen_nodes = set()
    current = head
    while current is not None:
        if current in seen_nodes:
            return 1
        seen_nodes.add(current)
        current = current.next
    return 0


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        extra = SinglyLinkedListNode(-1)
        temp = llist.head

        for i in range(llist_count):
            if i == index:
                extra = temp

            if i != llist_count - 1:
                temp = temp.next

        temp.next = extra

        result = has_cycle(llist.head)

        fptr.write(str(int(result)) + "\n")

    fptr.close()
