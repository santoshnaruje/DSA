# Rearrange array elements by sign (LeetCode 2149)
# Alternate positives and negatives starting with positive
# Created by santosh

class Solution:
    def rearrange_array(self, nums: list[int]) -> list[int]:
        """
        Two-index approach: positives at even indices, negatives at odd.
        Time: O(n), Space: O(n)
        """
        ans = [0] * len(nums)
        pos = 0
        neg = 1

        for x in nums:
            if x > 0:
                ans[pos] = x
                pos += 2
            else:
                ans[neg] = x
                neg += 2

        return ans


if __name__ == "__main__":
    s = Solution()
    nums = [3, 1, -2, -5, 2, -4]
    print(s.rearrange_array(nums))
