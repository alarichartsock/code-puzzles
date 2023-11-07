# First solution
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ret = ''

        arr1 = list(word1)
        arr2 = list(word2)

        i = 0

        while ((len(arr1) > 0) and (len(arr2) > 0)):
            ret += arr1.pop(0)
            ret += arr2.pop(0)
            i += 1

        if len(arr1) == 0 and len(arr2) > 0:
            ret += ''.join(word2[i:])
        elif len(arr1) > 0 and len(arr2) == 0:
            ret += ''.join(word1[i:])
        # else both words are exhausted

        return ret

# Revised solution
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        ret = ''

        while i <= len(word1) or i <= len(word2):
            if i >= len(word1):
                pass
            else:
                ret += word1[i]
            if i >= len(word2):
                pass
            else:
                ret += word2[i]
            i += 1
        
        return ret

# revised again
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = min(len(word1),len(word2))
        ret = ''
        for idx, (c1, c2) in enumerate(zip(word1,word2)):
            ret += c1 + c2
        ret += word1[m:] + word2[m:]
        return ret


