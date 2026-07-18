# 3Sum - Find triplets that add up to zero (LeetCode 15)
# Created by santosh

class Solution:
    def find_triplets(self, nums: list[int]) -> list[list[int]]:
        """
        Sort + two-pointer approach.
        Time: O(n^2), Space: O(1) (excluding output)
        """
        nums.sort()
        ans = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                triplet_sum = nums[i] + nums[left] + nums[right]

                if triplet_sum == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif triplet_sum > 0:
                    right -= 1
                else:
                    left += 1

        return ans


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    obj = Solution()
    ans = obj.find_triplets(nums)
    for triplet in ans:
        print(triplet)
