# Missing elements in a sorted array
# Created by santosh

def missing_elements_method1(nums: list[int]) -> list[int]:
    """
    Iterate through consecutive pairs and fill gaps.
    Time: O(n + m), Space: O(m)
    """
    result = []
    for i in range(len(nums) - 1):
        if nums[i + 1] - nums[i] != 1:
            j = nums[i] + 1
            while j < nums[i + 1]:
                result.append(j)
                j += 1
    return result


def missing_elements_method2(nums: list[int]) -> list[int]:
    """
    Uses a hash array to mark existing elements.
    Time: O(n + max_el), Space: O(max_el)
    """
    result = []
    max_el = max(nums)
    min_el = min(nums)
    hash_map = [0] * (max_el + 1)

    for num in nums:
        hash_map[num] += 1

    for i in range(min_el, len(hash_map) - 1):
        if hash_map[i] == 0:
            result.append(i)

    return result


# Time complexity - O(n + m)
# n - all elements in the array
# m - missing elements
# Space Complexity: O(m) where m is the number of missing elements


if __name__ == "__main__":
    nums = [1, 2, 3, 6, 7, 8, 12, 24]

    method1_result = missing_elements_method1(nums)
    print("Missing elements (method 1):", method1_result)

    method2_result = missing_elements_method2(nums)
    print("Missing elements (method 2):", method2_result)
