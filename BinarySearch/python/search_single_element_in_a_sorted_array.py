# Search Single Element in a Sorted Array (LeetCode 540)
# Created by santosh

class Solution:
    @staticmethod
    def single_non_duplicate(nums: list[int]) -> int:
        """
        Binary search to find element that appears exactly once.
        Every other element appears exactly twice.
        Time: O(log n), Space: O(1)
        """
        n = len(nums)

        if n == 1:
            return nums[0]

        if nums[0] != nums[1]:
            return nums[0]

        if nums[n - 1] != nums[n - 2]:
            return nums[n - 1]

        low = 1
        high = n - 2

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]

            # If on left side of single element, pairs start at even indices
            if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or \
               (mid % 2 == 1 and nums[mid] == nums[mid - 1]):
                low = mid + 1
            else:
                high = mid - 1

        return -1


if __name__ == "__main__":
    nums = [3, 3, 7, 7, 10, 11, 11]
    s = Solution()
    print(s.single_non_duplicate(nums))  # Expected: 10
