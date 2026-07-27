# Binary Search to find x in a sorted array (LeetCode 704)
# Created by santosh

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Standard binary search.
        Time: O(log n), Space: O(1)
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 9, 10]
    s = Solution()
    result = s.search(arr, 8)
    print(result)
