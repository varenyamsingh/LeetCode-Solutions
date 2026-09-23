class Solution:
    def minOperations(self, nums, x):
        target = sum(nums) - x

        # If target < 0, impossible
        if target < 0:
            return -1

        # If target == 0, remove everything
        if target == 0:
            return len(nums)

        left = 0
        current_sum = 0
        max_length = -1

        for right in range(len(nums)):
            current_sum += nums[right]

            # Shrink window if sum becomes too large
            while current_sum > target:
                current_sum -= nums[left]
                left += 1

            # Found a subarray with required sum
            if current_sum == target:
                max_length = max(max_length, right - left + 1)

        if max_length == -1:
            return -1

        return len(nums) - max_length