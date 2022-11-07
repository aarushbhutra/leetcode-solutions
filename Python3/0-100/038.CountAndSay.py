class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            res = "1"
            for i in range(n - 1):
                res = self.count(res)
            return res

    def count(self, s):
        res = ""
        i = 0
        while i < len(s):
            count = 1
            while i < len(s) - 1 and s[i] == s[i + 1]:
                count += 1
                i += 1
            res += str(count) + s[i]
            i += 1
        return res