# Remove duplicates from a sorted array
# Created by santosh

class Solution:
    def remove_duplicates(self, nums: list[int]) -> int:
        """
        Uses a set to track seen elements.
        Time: O(n), Space: O(k) where k = unique elements
        """
        index = 0
        seen: set[int] = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
                nums[index] = num
                index += 1
        return index

    def remove_duplicates_optimal(self, nums: list[int]) -> int:
        """
        Two-pointer approach for sorted array.
        Time: O(n), Space: O(1)
        """
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
        return i + 1


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4]
    s = Solution()
    m = s.remove_duplicates_optimal(nums)
    print(m)
    print("Array after removing duplicates:", nums[:m])
