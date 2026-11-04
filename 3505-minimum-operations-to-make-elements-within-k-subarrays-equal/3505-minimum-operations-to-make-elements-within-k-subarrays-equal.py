from sortedcontainers import SortedList
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:

        n = len(nums)
        m = n - x + 1

        sl = SortedList()
        costs = []

        # Coordinate compression
        vals = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(vals)}
        size = len(vals)

        bit_count = [0] * (size + 1)
        bit_sum = [0] * (size + 1)

        def update(bit, i, delta):
            while i <= size:
                bit[i] += delta
                i += i & -i

        def query(bit, i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        def kth(k):
            idx = 0
            step = 1 << (size.bit_length() - 1)

            while step:
                nxt = idx + step
                if nxt <= size and bit_count[nxt] < k:
                    idx = nxt
                    k -= bit_count[nxt]
                step >>= 1

            return idx + 1

        def get_cost():
            median_idx = kth((x + 1) // 2)
            median = vals[median_idx - 1]

            left_count = query(bit_count, median_idx)
            left_sum = query(bit_sum, median_idx)

            total_sum = query(bit_sum, size)

            right_count = x - left_count
            right_sum = total_sum - left_sum

            return (
                median * left_count - left_sum
                + right_sum - median * right_count
            )

        # Sliding window
        for i, num in enumerate(nums):

            idx = rank[num]
            update(bit_count, idx, 1)
            update(bit_sum, idx, num)

            if i >= x:
                old = nums[i - x]
                old_idx = rank[old]

                update(bit_count, old_idx, -1)
                update(bit_sum, old_idx, -old)

            if i >= x - 1:
                costs.append(get_cost())

        # DP
        INF = float('inf')

        dp = [[INF] * (k + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):

                dp[i][j] = dp[i - 1][j]

                if i >= x:
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i - x][j - 1] + costs[i - x]
                    )

        return dp[n][k]