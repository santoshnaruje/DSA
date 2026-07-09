# Longest subarray with given sum k
# Created by santosh

class Solution:
    def get_longest_sub_array_with_sum_k_using_hash_map(
        self, nums: list[int], k: int
    ) -> int:
        """
        Uses prefix sum + hashmap.
        Time: O(n), Space: O(n)
        """
        max_sub_array = 0
        total = 0
        mp: dict[int, int] = {}

        for i in range(len(nums)):
            total += nums[i]
            remaining = total - k

            if total == k:
                max_sub_array = max(max_sub_array, i + 1)

            if remaining in mp:
                max_sub_array = max(max_sub_array, i - mp[remaining])

            if total not in mp:
                mp[total] = i

        return max_sub_array

    def get_longest_sub_array_with_sum_k(self, nums: list[int], k: int) -> int:
        """
        Two-pointer / sliding window approach.
        Works only for non-negative numbers.
        Time: O(n), Space: O(1)
        """
        i = 0
        j = 0
        max_sub_array = 0
        total = 0
        n = len(nums)

        while j < n:
            total += nums[j]
            while i < j and total > k:
                total -= nums[i]
                i += 1
            if total == k:
                max_sub_array = max(max_sub_array, j - i + 1)
            j += 1

        return max_sub_array

    def two_sum(self, nums: list[int], target: int) -> list[int]:
        mp: dict[int, int] = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in mp:
                return [mp[needed], i]
            if num not in mp:
                mp[num] = i
        return [-1, -1]


# Leet code related problems:
# | NAME OF THE PROBLEM                                    | LEETCODE # | APPROACH                                              |
# | Two Sum                                                | 1          | Store num -> index; check target - num                |
# | Subarray Sum Equals K                                  | 560        | prefix sum -> frequency; count (sum - k)              |
# | Maximum Size Subarray Sum Equals K                     | 325        | prefix sum -> first index for longest length          |
# | Contiguous Array                                       | 525        | Convert 0 -> -1; prefix sum -> first index            |
# | Binary Subarrays With Sum                              | 930        | prefix sum -> frequency; count subarrays = goal       |
# | Subarray Sums Divisible by K                           | 974        | remainder -> frequency of prefix sums mod k           |
# | Continuous Subarray Sum                                | 523        | remainder -> first index; same remainder gap >= 2     |
# | Make Sum Divisible by P                                | 1590       | remainder -> index; find shortest subarray to remove  |
# | Longest Well-Performing Interval                       | 1124       | Convert hours > 8 -> +1 else -1; prefix sum -> index  |


if __name__ == "__main__":
    s = Solution()
    nums = [2, 7, 11, 15]
    k = 9
    print("Two Sum indices:", s.two_sum(nums, k))
    print("Longest subarray (hashmap):", s.get_longest_sub_array_with_sum_k_using_hash_map([1, 2, 3, 1, 1, 1], 3))
    print("Longest subarray (sliding window):", s.get_longest_sub_array_with_sum_k([1, 2, 3, 1, 1, 1], 3))
