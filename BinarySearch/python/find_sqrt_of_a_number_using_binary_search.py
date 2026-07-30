# Find square root of a number using binary search (LeetCode 69)
# Created by santosh

class Solution:
    def find_sqrt(self, n: int) -> int:
        """
        Binary search for integer square root.
        Time: O(log n), Space: O(1)
        """
        left = 1
        right = n // 2
        ans = -1

        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid <= n:
                ans = mid
                left = mid + 1
            elif mid * mid > n:
                right = mid - 1

        return ans


if __name__ == "__main__":
    n = 36
    obj = Solution()
    print(obj.find_sqrt(n))
