class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        chars = list(pattern)

        d = {}
        e = {}

        i = 0

        if len(words) != len(chars):
            return False

        while i < len(words):
            if chars[i] in d and d[chars[i]] != words[i]:
                return False

            if words[i] in e and e[words[i]] != chars[i]:
                return False

            d[chars[i]] = words[i]
            e[words[i]] = chars[i]

            i += 1
        
        return True