# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        stack = []
        cur = head

        while cur is not None:
            stack.append(cur.val)
            cur = cur.next

        if len(queue) == 0:
            return None

        cur = ListNode(stack.pop(-1))
        ret = cur

        while len(queue) > 0:
            cur.next = ListNode(stack.pop(-1))
            cur = cur.next

        return ret
