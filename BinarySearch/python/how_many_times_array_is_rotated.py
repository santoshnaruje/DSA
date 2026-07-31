# How many times has the sorted array been rotated?
# Equivalent to finding the index of the minimum element.
# Created by santosh

class Solution:
    def get_how_many_times_array_is_rotated(self, nums: list[int]) -> int:
        """
        Binary search to find index of minimum element (= rotation count).
        Time: O(log n), Space: O(1)
        """
        low, high = 0, len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return low


if __name__ == "__main__":
    s = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2, 3]
    print(s.get_how_many_times_array_is_rotated(nums))
