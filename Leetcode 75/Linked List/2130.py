# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        pairs = [head.val]
        cur = head

        while cur.next:
            cur = cur.next
            pairs.append(cur.val)

        mid = len(pairs) // 2

        if len(pairs) <= 2:
            return sum(pairs)

        sums = []

        for i,j in zip(pairs[:mid], reversed(pairs[mid:])):
            sums.append(i+j)

        return max(sums)