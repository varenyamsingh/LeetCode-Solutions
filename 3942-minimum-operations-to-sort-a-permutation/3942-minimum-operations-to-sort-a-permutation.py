class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        pos = nums.index(0)

        inc = True
        dec = True

        for i in range(n):
            a = nums[i]
            b = nums[(i + 1) % n]

            if b != (a + 1) % n:
                inc = False

            if b != (a - 1) % n:
                dec = False

        ans = float('inf')

        if inc:
            # Rotate left, or simulate right rotations
            ans = min(pos, n - pos + 2)

        if dec:
            # Reverse orientation, then rotate
            k = n - 1 - pos
            ans = min(ans, 1 + min(k, n - k))

        return ans if ans != float('inf') else -1