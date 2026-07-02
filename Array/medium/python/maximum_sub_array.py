from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        start = 0
        end = 0
        tempStart = 0
        maxSum = float('-inf')
        for i in range(len(nums)):
            sum += nums[i]
            if sum > maxSum:
                maxSum = sum
                start = tempStart
                end = i

            if sum < 0 :
                sum = 0
                tempStart = i + 1

        for i in range(start, end + 1):
            print(nums[i], end=" ")
        print()
        return maxSum


if __name__ == '__main__':
    nums = [2, 3, 5, -2, 7, -4]
    print(Solution().maxSubArray(nums))
