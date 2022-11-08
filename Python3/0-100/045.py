class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        end = 0
        max_position = 0
        steps = 0
        for i in range(n - 1):
            max_position = max(max_position, i + nums[i])
            if i == end:
                end = max_position
                steps += 1
        return steps