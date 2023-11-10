class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []

        ret = []

        for char in s:
            if char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                vowels.append(char)
                ret.append('👾')
            else:
                ret.append(char)

        for i,char in enumerate(ret):
            if char == '👾':
                ret[i] = vowels.pop(-1)
        
        return ''.join(ret)