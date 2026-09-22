class Solution:
    def canJump(self, nums):
        n = len(nums)

        dp = [False] * n
        dp[0] = True

        for i in range(n):
            if not dp[i]:
                continue

            for j in range(i + 1, min(n, i + nums[i] + 1)):
                dp[j] = True

        return dp[-1]