# Longest consecutive sequence in an array (LeetCode 128)
# Created by santosh

class Solution:
    def get_longest_sequence(self, nums: list[int]) -> int:
        """
        HashSet approach: only start counting from sequence beginners.
        Time: O(n), Space: O(n)
        """
        unique_elements = set(nums)
        longest_sequence = float('-inf')

        for num in unique_elements:
            # Only start a sequence from its beginning
            if (num - 1) not in unique_elements:
                count = 1
                x = num
                while (x + 1) in unique_elements:
                    count += 1
                    x += 1
                longest_sequence = max(longest_sequence, count)

        return longest_sequence


if __name__ == "__main__":
    s = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    print(s.get_longest_sequence(nums))  # Expected: 4 (1,2,3,4)
