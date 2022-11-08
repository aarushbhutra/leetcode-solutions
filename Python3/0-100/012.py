class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        integer = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        i = 0
        res = ""
        while num > 0:
            for _ in range(num // integer[i]):
                res += roman[i]
                num -= integer[i]
            i += 1
        return res