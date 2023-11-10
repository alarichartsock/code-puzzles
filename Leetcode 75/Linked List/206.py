# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        queue = []
        cur = head

        while cur is not None:
            queue.append(cur.val)
            cur = cur.next

        if len(queue) == 0:
            return None

        cur = ListNode(queue.pop(-1))
        ret = cur

        while len(queue) > 0:
            cur.next = ListNode(queue.pop(-1))
            cur = cur.next

        return ret
