class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_len = len(words[0])
        word_num = len(words)
        s_len = len(s)
        res = []
        for i in range(s_len - word_len * word_num + 1):
            if s[i:i + word_len] in words:
                temp = words[:]
                j = i
                while j < s_len and s[j:j + word_len] in temp:
                    temp.remove(s[j:j + word_len])
                    j += word_len
                if not temp:
                    res.append(i)
        return res