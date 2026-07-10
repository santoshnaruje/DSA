# Maximum consecutive ones in a binary array
# Created by santosh

class Solution:
    def maximum_consecutive_ones(self, nums: list[int]) -> int:
        max_count = 0
        count = 0
        for num in nums:
            if num == 0:
                max_count = max(max_count, count)
                count = 0
            else:
                count += 1
                max_count = max(max_count, count)
        return max_count


if __name__ == "__main__":
    nums = [1, 1, 0, 1, 1, 1]
    s = Solution()
    print(s.maximum_consecutive_ones(nums))
