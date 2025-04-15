# Problem: https://leetcode.com/problems/merge-k-sorted-lists/description/
## Alt: https://www.geeksforgeeks.org/merge-k-sorted-arrays/
## Alt: https://www.geeksforgeeks.org/merge-k-sorted-arrays-set-2-different-sized-arrays/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists) == 0:
            return None

        interval = 1
        while interval < len(lists):
            for ptr in range(0, len(lists) - interval, interval * 2):
                lists[ptr] = self.merge(lists[ptr], lists[ptr + interval])
            interval *= 2
        return lists[0]

    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2
