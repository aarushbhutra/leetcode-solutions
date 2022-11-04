class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        if s:
            return len(s[-1])
        else:
            return 0