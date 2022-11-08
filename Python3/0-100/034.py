class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left_index, right_index = mid, mid
                while left_index - 1 >= 0 and nums[left_index - 1] == target:
                    left_index -= 1
                while right_index + 1 < len(nums) and nums[right_index + 1] == target:
                    right_index += 1
                return [left_index, right_index]
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return [-1, -1]