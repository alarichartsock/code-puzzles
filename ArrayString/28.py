class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            for i,letter in enumerate(haystack):
                if needle == haystack[i:len(needle)+i]:
                    return i