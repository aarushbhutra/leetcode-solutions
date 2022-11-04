class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        else:
            left = 0
            right = x
            while left <= right:
                mid = left + (right - left) // 2
                if mid ** 2 == x:
                    return mid
                elif mid ** 2 < x:
                    left = mid + 1
                    res = mid
                else:
                    right = mid - 1
            return res