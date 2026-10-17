
class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        def digit_sum(num):
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total

        target = sorted(nums, key=lambda x: (digit_sum(x), x))

        pos = {num: i for i, num in enumerate(nums)}

        swaps = 0

        for i in range(len(nums)):
            if nums[i] != target[i]:

                correct = target[i]
                j = pos[correct]

                pos[nums[i]] = j
                pos[correct] = i

                nums[i], nums[j] = nums[j], nums[i]

                swaps += 1

        return swaps
