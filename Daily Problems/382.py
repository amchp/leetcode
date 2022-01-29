# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from random import choice
class Solution:
    #I did it the easy dumb way of passing the list to a non-link list
    #I read a very convoluted solution using sample sizes
    def __init__(self, head: Optional[ListNode]):
        self.l = []
        cur = head
        while cur:
            self.l.append(cur.val)
            cur = cur.next

    def getRandom(self) -> int:
        return choice(self.l)