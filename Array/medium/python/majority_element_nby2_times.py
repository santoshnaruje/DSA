# Majority element appearing more than n/2 times (LeetCode 169)
# Boyer-Moore Voting Algorithm
# Created by santosh

class Solution:
    def majority_element(self, nums: list[int]) -> int:
        """
        Boyer-Moore Voting Algorithm.
        Time: O(n), Space: O(1)
        """
        count = 0
        candidate = nums[0]

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        # Verify the candidate
        count = sum(1 for num in nums if num == candidate)
        if count > len(nums) // 2:
            return candidate

        return -1


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 1, 2]
    s = Solution()
    print(s.majority_element(nums))
