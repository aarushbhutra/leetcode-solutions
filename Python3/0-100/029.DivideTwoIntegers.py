class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        if dividend > 0 and divisor > 0:
            return self.dividePositive(dividend, divisor)
        elif dividend > 0 and divisor < 0:
            return -self.dividePositive(dividend, -divisor)
        elif dividend < 0 and divisor > 0:
            return -self.dividePositive(-dividend, divisor)
        else:
            return self.dividePositive(-dividend, -divisor)

    def dividePositive(self, dividend: int, divisor: int) -> int:
        if dividend < divisor:
            return 0
        count = 1
        sum = divisor
        while sum + sum <= dividend:
            count = count + count
            sum = sum + sum
        return count + self.dividePositive(dividend - sum, divisor)