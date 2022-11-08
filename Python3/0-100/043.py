class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                res[i + j + 1] += int(num1[i]) * int(num2[j])
        for i in range(len(res) - 1, 0, -1):
            res[i - 1] += res[i] // 10
            res[i] %= 10
        return "".join([str(x) for x in res]).lstrip("0")

        