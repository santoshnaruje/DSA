# Sort an array of 0s, 1s and 2s (Dutch National Flag Algorithm) (LeetCode 75)
# Created by santosh

class Solution:
    def selection_sort(self, nums: list[int]) -> None:
        """Selection sort O(n^2)"""
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

    def dutch_national_flag_algorithm(self, nums: list[int]) -> None:
        """
        Dutch National Flag Algorithm (Three-way partition).
        Time: O(n), Space: O(1)
        """
        left = 0
        high = len(nums) - 1
        mid = 0

        while mid <= high:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


if __name__ == "__main__":
    s = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    s.dutch_national_flag_algorithm(nums)
    print(nums)
