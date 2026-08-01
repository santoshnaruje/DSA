# Lower and Upper Bound + related utilities
# Created by santosh

import bisect


class Solution:
    def lower_bound(self, nums: list[int], target: int, low: int, high: int) -> int:
        """
        Returns the index of the first element >= target.
        Recursive approach. Time: O(log n)
        """
        if low > high:
            return low
        mid = low + (high - low) // 2
        if nums[mid] >= target:
            return self.lower_bound(nums, target, low, mid - 1)
        return self.lower_bound(nums, target, mid + 1, high)

    def upper_bound(self, nums: list[int], target: int, low: int, high: int) -> int:
        """
        Returns the index of the first element > target.
        Recursive approach. Time: O(log n)
        """
        if low > high:
            return low
        mid = low + (high - low) // 2
        if nums[mid] > target:
            return self.upper_bound(nums, target, low, mid - 1)
        return self.upper_bound(nums, target, mid + 1, high)

    def search_insert(self, nums: list[int], target: int, low: int, high: int) -> int:
        """Returns the position where target should be inserted."""
        if low > high:
            return low
        mid = low + (high - low) // 2
        if nums[mid] >= target:
            return self.lower_bound(nums, target, low, mid - 1)
        return self.lower_bound(nums, target, mid + 1, high)

    def floor_value(self, nums: list[int], target: int, low: int, high: int) -> int:
        """Returns the largest element <= target."""
        return nums[self.upper_bound(nums, target, low, high) - 1]

    def ceil_value(self, nums: list[int], target: int, low: int, high: int) -> int:
        """Returns the smallest element >= target."""
        return nums[self.lower_bound(nums, target, low, high)]

    def last_occurrence_in_sorted_array(
        self, nums: list[int], target: int, low: int, high: int
    ) -> int:
        """Returns index of first occurrence of target, or -1 if not found."""
        idx = self.lower_bound(nums, target, low, high)
        if idx < len(nums) and nums[idx] >= target:
            return idx
        return -1


if __name__ == "__main__":
    nums = [3, 4, 13, 13, 13, 20, 40]
    target = 60
    low = 0
    high = len(nums) - 1
    s = Solution()

    # print("Lower bound:", s.lower_bound(nums, target, low, high))
    # print("Upper bound:", s.upper_bound(nums, target, low, high))
    # print("Search insert:", s.search_insert(nums, 5, low, high))
    # print("Ceil value:", s.ceil_value(nums, target, low, high))
    # print("Floor value:", s.floor_value(nums, target, low, high))
    print("Last occurrence index:", s.last_occurrence_in_sorted_array(nums, target, low, high))
