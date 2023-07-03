# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # two pointers, one for the end, one for the middle
        # middle pointer increments by one for every two the end pointer increments
        # since second middle is returned, the pointers will be incremented as such:
        #   1. end pointer increments
        #   2. if end pointer not None, middle increments
        #   3. end pointer increments. return if None
        # this guarantees that the middle pointer will always point at the second
        # middle (if there are two), and the end pointer will track when a return
        # is appropriate
        mid, end = head, head
        while True:
            end = end.next
            if end is None:
                return mid
            mid = mid.next
            end = end.next
            if end is None: 
                return mid
