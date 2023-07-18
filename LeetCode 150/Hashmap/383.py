class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}

        for c in magazine:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        
        for c in ransomNote:
            if c not in d:
                return False

            if d[c] > 0:
                d[c] -= 1
            else: 
                return False

        return True