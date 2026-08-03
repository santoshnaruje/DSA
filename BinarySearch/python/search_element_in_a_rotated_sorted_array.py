# Search element in a rotated sorted array (LeetCode 33 & 81)
# Created by santosh

class Solution:
    def get_search_without_duplicates(self, nums: list[int], target: int) -> int:
        """
        Search in rotated sorted array (no duplicates). LeetCode 33.
        Time: O(log n), Space: O(1)
        """
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Right half is sorted
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

    def get_search_with_duplicates(self, nums: list[int], target: int) -> int:
        """
        Search in rotated sorted array (with duplicates). LeetCode 81.
        Time: O(log n) average, O(n) worst case
        """
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid

            # Handle duplicates
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue

            # Left half is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1


if __name__ == "__main__":
    s = Solution()
    nums = [1, 3, 1, 1, 1]
    target = 3
    print(s.get_search_without_duplicates(nums, target))
