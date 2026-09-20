import string

class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0

        for i, ch in enumerate(s, 1):
            reverse_position = 26 - string.ascii_lowercase.index(ch)
            ans += reverse_position * i

        return ans