# Pair of elements with sum k (sorted array)
# Created by santosh

def pair_of_elements_with_sum(nums: list[int], k: int) -> list[tuple[int, int]]:
    """Brute force: O(n^2)"""
    res = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == k:
                res.append((nums[i], nums[j]))
    return res


def pair_of_elements_using_2_pointer(nums: list[int], k: int) -> list[tuple[int, int]]:
    """Two-pointer approach for sorted array: O(n)"""
    res = []
    i, j = 0, len(nums) - 1
    while i <= j:
        s = nums[i] + nums[j]
        if s == k:
            res.append((nums[i], nums[j]))
            i += 1
            j -= 1
        elif s > k:
            j -= 1
        else:
            i += 1
    return res


def pair_of_elements_using_hash_map(nums: list[int], k: int) -> list[list[int]]:
    """Hash set approach: O(n)"""
    res = []
    seen: set[int] = set()
    for x in nums:
        target = k - x
        if target in seen:
            res.append([x, target])
        else:
            seen.add(x)
    return res


if __name__ == "__main__":
    arr = [6, 3, 8, 10, 16, 7, 5, 2, 9, 14]
    arr.sort()
    total = 15

    print("2-pointer:", pair_of_elements_using_2_pointer(arr, total))
    print("HashMap:", pair_of_elements_using_hash_map(arr, total))
