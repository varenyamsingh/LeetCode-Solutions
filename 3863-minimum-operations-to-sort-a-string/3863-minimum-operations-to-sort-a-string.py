class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        if s == ''.join(sorted(s)):
            return 0

        if n == 2:
            return -1

        lo = min(s)
        hi = max(s)

        if s[0] == lo or s[-1] == hi:
            return 1

        if (s[0] == hi and s.count(hi) == 1
                and s[-1] == lo and s.count(lo) == 1):
            return 3

        return 2
