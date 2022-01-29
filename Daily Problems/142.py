# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #This was an interesting problem because I remembered the solution from a youtube video
    #Although I still needed to remind myself exactly how to program the problem
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None
        turtle = head.next
        hair = head.next.next
        while hair != None:
            if turtle == hair:
                turtle = head
                while turtle != hair:
                    turtle = turtle.next
                    hair = hair.next
                return turtle
            turtle = turtle.next
            hair = hair.next
            if hair != None:
                hair = hair.next
        return None
            