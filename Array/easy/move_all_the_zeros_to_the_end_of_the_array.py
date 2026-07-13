# Move all zeros to the end of the array
# Created by santosh

class Solution:
    def move_zeros_to_the_end(self, nums: list[int]) -> None:
        """Brute force: collect non-zeros, fill rest with zeros."""
        res = [num for num in nums if num != 0]
        count = len(res)
        for i in range(count):
            nums[i] = res[i]
        for i in range(count, len(nums)):
            nums[i] = 0

    def move_zeros_to_the_end_optimal(self, nums: list[int]) -> None:
        """
        Optimal two-pointer approach.
        Time: O(n), Space: O(1)
        """
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] == 0:
                j += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1


if __name__ == "__main__":
    nums = [1, 0, 2, 3, 0, 4, 0, 1]
    s = Solution()
    s.move_zeros_to_the_end_optimal(nums)
    print(nums)
