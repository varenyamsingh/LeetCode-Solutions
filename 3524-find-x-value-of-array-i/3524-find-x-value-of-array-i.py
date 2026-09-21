class Solution:
    def resultArray(self, nums, k):
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            num %= k
            new_dp = [0] * k

            # Single-element subarray
            new_dp[num] += 1

            # Previous subarrays + current number
            for r in range(k):
                new_r = (r * num) % k
                new_dp[new_r] += dp[r]

            dp = new_dp

            for r in range(k):
                ans[r] += dp[r]

        return ans