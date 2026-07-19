# 4Sum Problem (LeetCode 18)
# Created by santosh

# TODO: Write a generic K sum problem

class Solution:
    def find_quadrants(self, nums: list[int], target: int) -> list[list[int]]:
        """
        Sort + two-pointer nested approach.
        Time: O(n^3), Space: O(1) (excluding output)
        """
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = len(nums) - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total > target:
                        right -= 1
                    else:
                        left += 1

        return result


if __name__ == "__main__":
    nums = [2, 2, 2, 2, 2]
    target = 8
    result = Solution().find_quadrants(nums, target)
    for quad in result:
        print(quad)
