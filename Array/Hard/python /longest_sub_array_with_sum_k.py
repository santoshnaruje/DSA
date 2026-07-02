from typing import List


class Solution:
    def longestSubArrayBruteForce(self, nums: List[int],k) -> int:
        max_len= float('-inf')
        for i in range(len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum += nums[j]
                if sum == k:
                    max_len = max(max_len, j - i + 1)

        return max_len

    def longestSubArrayOptimal(self,nums,k):
        max_len= float('-inf')
        seen ={}
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum == k:
                max_len = max(max_len, i+1)
            elif sum in seen:
                max_len = max(max_len, i- seen[sum])
            else:
                seen[sum] = i

        return max_len






if __name__=='__main__':
    array = [9, -3, 3, -1, 6, -5]
    solution = Solution()
    result = solution.longestSubArrayOptimal(array,0)
    print(result)








