
import math

class Solution:
    def smallestDivisor(self, nums,threshold):
        def get_divisor_sum(nums, mid):
            return sum(math.ceil(num / mid  ) for num in nums)
        low = 1
        high = max(nums)
        answer = -1
        while low <= high :
            mid = (low + high) // 2
            res = get_divisor_sum(nums, mid)
            if res <= threshold:
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        return answer




if __name__ == '__main__':
    nums = [44,22,33,11,1]
    threshhold = 5
    Sol = Solution()
    res = Sol.smallestDivisor(nums,threshhold)
    print(res)