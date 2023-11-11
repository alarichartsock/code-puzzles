class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        total = 0

        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                total = 1
        else:
            for i,pot in enumerate(flowerbed):
                if pot == 0:
                    if i == 0:
                        if flowerbed[i+1] != 1:
                            flowerbed[i] = 1
                            total += 1
                    elif i == len(flowerbed) - 1:
                        if flowerbed[i-1] != 1:
                            flowerbed[i] = 1
                            total += 1
                    else:
                        if flowerbed[i-1] != 1 and flowerbed[i+1] != 1:
                            flowerbed[i] = 1
                            total += 1
        
        if total >= n:
            return True
        else:
            return False