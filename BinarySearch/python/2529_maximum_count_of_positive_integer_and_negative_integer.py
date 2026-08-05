# Maximum Count of Positive Integer and Negative Integer (LeetCode 2529)
# Created by santosh

import bisect


class Solution:
    def max_count(self, nums: list[int]) -> int:
        """
        Binary search to find first positive and first zero.
        Time: O(log n), Space: O(1)
        """
        n = len(nums)

        # Find first positive index
        left, right = 0, n - 1
        first_pos = n
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > 0:
                first_pos = mid
                right = mid - 1
            else:
                left = mid + 1

        # Find first zero index
        left, right = 0, n - 1
        first_zero = n
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= 0:
                first_zero = mid
                right = mid - 1
            elif nums[mid] < 0:
                left = mid + 1

        return max(first_zero, n - first_pos)


if __name__ == "__main__":
    s = Solution()
    nums = [-2, -1, -1, 1, 2, 3]
    print(s.max_count(nums))
