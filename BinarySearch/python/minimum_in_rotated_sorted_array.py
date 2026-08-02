# Minimum in rotated sorted array (LeetCode 153 & 154)
# Created by santosh

class Solution:
    @staticmethod
    def get_minimum_element_in_rotated_sorted_array_with_duplicates(
        nums: list[int],
    ) -> int:
        """
        Handles duplicates by shrinking both ends.
        Time: O(log n) average, O(n) worst case with duplicates
        """
        low, high = 0, len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2

            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return nums[low]

    @staticmethod
    def get_minimum_element_in_rotated_sorted_array(nums: list[int]) -> int:
        """
        No duplicates version.
        Time: O(log n), Space: O(1)
        """
        low, high = 0, len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return nums[low]


if __name__ == "__main__":
    nums = [4, 5, 1, 2, 3]
    s = Solution()
    print(s.get_minimum_element_in_rotated_sorted_array(nums))
