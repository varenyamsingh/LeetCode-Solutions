
class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)

        def can_sort(k):
            prev_max = float('-inf')

            for start in range(0, n, k):
                mn = float('inf')
                mx = float('-inf')
                drops = 0

                for j in range(start, start + k):
                    x = nums[j]
                    mn = min(mn, x)
                    mx = max(mx, x)

                    nxt = nums[start] if j == start + k - 1 else nums[j + 1]

                    if x > nxt:
                        drops += 1

                if drops > 1 or mn < prev_max:
                    return False

                prev_max = mx

            return True

        ans = 0

        for d in range(1, int(n ** 0.5) + 1):
            if n % d == 0:
                if can_sort(d):
                    ans += d

                other = n // d

                if other != d and can_sort(other):
                    ans += other

        return ans
