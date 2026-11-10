
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:

        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = float('inf')

            for j in range(max(0, i - 3), i):
                dp[i] = min(
                    dp[i],
                    dp[j] + costs[i - 1] + (i - j) ** 2
                )

        return dp[n]
