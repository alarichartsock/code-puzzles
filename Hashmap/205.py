class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        i = 0
        d = {}
        e = {}

        while i < len(s):
            
            if s[i] in d and (d[s[i]] != t[i]):
                return False

            if t[i] in e and (e[t[i]] != s[i]):
                return False

            d[s[i]] = t[i]
            e[t[i]] = s[i]
            print(f'{d[s[i]]} {s[i]} {t[i]}')
            i += 1
        
        return True