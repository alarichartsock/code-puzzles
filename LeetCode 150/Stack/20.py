# BlackRock asked me for this one
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mappings = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        if len(s) <= 1:
            return False

        for char in s:
            if char in mappings.values():
                stack.append(char)
            if char in mappings.keys():
                if len(stack) == 0:
                    return False

                val = stack.pop(-1)
                if val == mappings[char]:
                    pass
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False