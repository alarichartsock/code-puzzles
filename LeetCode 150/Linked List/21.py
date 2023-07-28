# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# This might be cheating. lol
class Solution:
    def iterateList(self, list):
        if list is None:
            return None

        while list.next is not None:
            yield list.val
            list = list.next
        
        yield list.val

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sort = sorted(list(self.iterateList(list1)) + list(self.iterateList(list2)))

        if len(sort) == 0:
            return None

        cur = ListNode(sort[0])
        head = cur

        for s in sort[1:]:
            nxt = ListNode(s)
            cur.next = nxt
            cur = nxt

        return head