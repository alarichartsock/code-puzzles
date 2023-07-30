class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        path = [s for s in path if len(s) > 0]

        stack = []

        for d in path:
            if d == '..':
                if len(stack) == 0:
                    pass
                else:
                    del stack[-1]
            elif d == '.':
                pass
            else:
                stack.append(d)
    
        return "/" + "/".join(stack)