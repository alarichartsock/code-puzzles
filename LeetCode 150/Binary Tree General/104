# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [root]

        ret = 0

        if stack[0] is None:
            return ret
        else:
            while stack[-1] is not None:
                cur = stack.pop(-1)
                if cur is None:
                    ret -= 1
                else:
                    ret += 1
                stack.append(cur.left)
                stack.append(cur.right)
        
        return ret
