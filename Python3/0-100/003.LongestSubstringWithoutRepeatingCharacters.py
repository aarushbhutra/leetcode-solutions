class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        used_char = {}
        for right in range(len(s)):
            if s[right] in used_char and left <= used_char[s[right]]:
                left = used_char[s[right]] + 1
            else:
                max_len = max(max_len, right - left + 1)
            used_char[s[right]] = right
        return max_len