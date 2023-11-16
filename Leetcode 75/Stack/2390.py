class Solution:
    def removeStars(self, s: str) -> str:
        ret = []

        for char in s:
            if char != '*':
                ret.append(char)
            else:
                ret.pop(-1)
    
        return ''.join(ret)