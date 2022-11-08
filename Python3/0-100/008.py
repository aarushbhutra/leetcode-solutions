class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        if s[0] == "-":
            s = s[1:]
            sign = -1
        elif s[0] == "+":
            s = s[1:]
            sign = 1
        else:
            sign = 1
        if not s:
            return 0
        if s[0].isdigit():
            for i in range(len(s)):
                if not s[i].isdigit():
                    s = s[:i]
                    break
            if s:
                s = sign * int(s)
                if s < -2**31:
                    return -2**31
                elif s > 2**31 - 1:
                    return 2**31 - 1
                else:
                    return s
            else:
                return 0
        else:
            return 0