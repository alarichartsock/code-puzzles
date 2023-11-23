class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 0

        while i < len(chars):
            cur = chars[i]
            count = 1
            while i+1 < len(chars) and cur == chars[i+1]:
                count += 1
                i += 1
            
            if i < len(chars) and count == 1:
                chars[j] = cur
            else:
                chars[j] = cur
                for s in list(str(count)):
                    chars[j+1] = s
                    j += 1
            j += 1
            i += 1
        
        return j