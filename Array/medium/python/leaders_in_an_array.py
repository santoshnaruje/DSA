# Leaders in an array
# An element is a leader if it is greater than all elements to its right.
# Created by santosh

class Solution:
    def get_leaders_in_array(self, nums: list[int]) -> list[int]:
        """
        Traverse from right to left keeping track of maximum.
        Time: O(n), Space: O(n)
        """
        result = []
        last_element = nums[-1]
        result.append(nums[-1])
        right = len(nums) - 2

        while right >= 0:
            if nums[right] > last_element:
                result.append(nums[right])
                last_element = nums[right]
            right -= 1

        result.reverse()
        return result


if __name__ == "__main__":
    s = Solution()
    nums = [10, 22, 12, 3, 0, 6]
    result = s.get_leaders_in_array(nums)
    print(" ".join(map(str, result)))
