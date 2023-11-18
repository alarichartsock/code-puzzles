# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        tot = 1

        nodes = {}

        while cur.next:
            nodes[tot] = cur
            cur = cur.next
            tot += 1

        if tot <= 1:
            return None

        prev = nodes[tot // 2]
        mid = prev.next
        prev.next = mid.next

        return head