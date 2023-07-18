class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0

        smallestLen = min([len(s) for s in strs])

        if len(strs) == 1 and len(strs[0]) > 0:
            return strs[0]

        if smallestLen == 0:
            return ""

        while i < smallestLen:
            for j in range(len(strs)-1):
                if(strs[j][i] != strs[j+1][i]):
                    print(f'{strs[j][i]} {strs[j+1][i]}')
                    return strs[j][:i]
            i += 1
        return strs[0][:i]