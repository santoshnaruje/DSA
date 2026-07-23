# Maximum subarray sum (Kadane's Algorithm) (LeetCode 53)
# Created by santosh

class Solution:
    def max_subarray_sum(self, nums: list[int]) -> int:
        """
        Kadane's Algorithm.
        Time: O(n), Space: O(1)
        """
        total = 0
        max_sum = float('-inf')
        start = 0
        end = 0
        temp_start = 0

        for i, num in enumerate(nums):
            if total == 0:
                temp_start = i
            total += num
            if total > max_sum:
                max_sum = total
                start = temp_start
                end = i
            if total < 0:
                total = 0

        print(f"Subarray indices: [{start}, {end}]")
        return max_sum


if __name__ == "__main__":
    nums = [2, 3, 5, -2, 7, -4]
    obj = Solution()
    print("Max subarray sum:", obj.max_subarray_sum(nums))
