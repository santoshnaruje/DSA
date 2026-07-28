# Count occurrences of a value in a sorted array
# Created by santosh

import bisect


class Solution:
    def count_of_occurrences_in_a_sorted_array(
        self, nums: list[int], target: int
    ) -> int:
        """
        Uses lower_bound and upper_bound (bisect_left and bisect_right).
        Time: O(log n), Space: O(1)
        """
        first_occurrence = bisect.bisect_left(nums, target)
        last_occurrence = bisect.bisect_right(nums, target)
        return last_occurrence - first_occurrence


if __name__ == "__main__":
    s = Solution()
    nums = [2, 2, 3, 3, 3, 3, 4]
    target = 3
    print(s.count_of_occurrences_in_a_sorted_array(nums, target))
