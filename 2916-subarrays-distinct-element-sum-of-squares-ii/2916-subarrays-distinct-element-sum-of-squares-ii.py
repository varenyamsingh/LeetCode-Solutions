
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        total = [0] * (4 * n)
        square = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, left, right, val):
            length = right - left + 1

            square[node] = (
                square[node]
                + 2 * val * total[node]
                + val * val * length
            ) % MOD

            total[node] = (
                total[node] + val * length
            ) % MOD

            lazy[node] += val

        def push(node, left, right):
            if lazy[node] == 0 or left == right:
                return

            mid = (left + right) // 2
            val = lazy[node]

            apply(node * 2, left, mid, val)
            apply(node * 2 + 1, mid + 1, right, val)

            lazy[node] = 0

        def update(node, left, right, ql, qr):
            if ql <= left and right <= qr:
                apply(node, left, right, 1)
                return

            push(node, left, right)

            mid = (left + right) // 2

            if ql <= mid:
                update(node * 2, left, mid, ql, qr)

            if qr > mid:
                update(node * 2 + 1, mid + 1, right, ql, qr)

            total[node] = (
                total[node * 2]
                + total[node * 2 + 1]
            ) % MOD

            square[node] = (
                square[node * 2]
                + square[node * 2 + 1]
            ) % MOD

        last_seen = {}
        ans = 0

        for r, num in enumerate(nums):
            prev = last_seen.get(num, -1)

            update(1, 0, n - 1, prev + 1, r)

            ans = (ans + square[1]) % MOD

            last_seen[num] = r

        return ans
