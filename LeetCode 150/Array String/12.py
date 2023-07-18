class Solution:
    def intToRoman(self, num: int) -> str:
        mappings = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
            4: 'IV',
            9: 'IX',
            40: 'XL',
            90: 'XC',
            400: 'CD',
            900: 'CM'
        }

        factors = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        rem = num
        ret = ''

        for factor in factors[start::-1]:
            while (rem - factor) >= 0 and rem > 0:
                ret += mappings[factor]
                rem -= factor
        return ret