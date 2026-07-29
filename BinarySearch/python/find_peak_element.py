# Find Peak Element (LeetCode 162)
# Created by santosh

class Solution:
    def find_peak_element(self, nums: list[int]) -> int:
        """
        Binary search for peak element.
        Time: O(log n), Space: O(1)
        """
        n = len(nums)

        if n == 1:
            return nums[0]

        if nums[0] > nums[1]:
            return nums[0]

        if nums[n - 1] > nums[n - 2]:
            return nums[n - 1]

        low = 1
        high = n - 2

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            elif nums[mid] > nums[mid + 1]:
                high = mid - 1

        return -1


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 1]
    print(s.find_peak_element(nums))
