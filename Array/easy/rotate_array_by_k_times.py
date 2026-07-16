# Rotate array by k times (left and right)
# Created by santosh

def left_rotate_array_by_k(nums: list[int], k: int) -> list[int]:
    """
    Brute force left rotate.
    Time: O(n+k), Space: O(k)
    """
    n = len(nums)
    k = k % n
    res = nums[:k]
    j = 0
    for i in range(k, n):
        nums[j] = nums[i]
        j += 1
    for el in res:
        nums[j] = el
        j += 1
    return nums


def right_rotate_array_by_k(nums: list[int], k: int) -> list[int]:
    """
    Brute force right rotate.
    Time: O(n+k), Space: O(k)
    """
    n = len(nums)
    k = k % n
    res = nums[n - k:]
    for i in range(n - k - 1, -1, -1):
        nums[i + k] = nums[i]
    for i in range(k):
        nums[i] = res[i]
    return nums


def optimal_right_rotate_array_by_k(nums: list[int], k: int) -> None:
    """
    Optimal right rotate using reversal algorithm.
    Time: O(n), Space: O(1)
    """
    n = len(nums)
    k = k % n
    # Step 1: Reverse entire array
    nums.reverse()
    # Step 2: Reverse first k elements
    nums[:k] = reversed(nums[:k])
    # Step 3: Reverse last n-k elements
    nums[k:] = reversed(nums[k:])


def optimal_left_rotate_array_by_k(nums: list[int], k: int) -> None:
    """
    Optimal left rotate using reversal algorithm.
    Time: O(n), Space: O(1)
    """
    n = len(nums)
    if n == 0:
        return
    k = k % n
    # Step 1: Reverse first k elements
    nums[:k] = reversed(nums[:k])
    # Step 2: Reverse last n-k elements
    nums[k:] = reversed(nums[k:])
    # Step 3: Reverse the whole array
    nums.reverse()


# Left or right rotate by brute force: Time O(n+k), Space O(k)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 3

    nums_copy = nums[:]
    optimal_right_rotate_array_by_k(nums_copy, k)
    print("Right rotate by", k, ":", nums_copy)

    nums_copy2 = nums[:]
    optimal_left_rotate_array_by_k(nums_copy2, k)
    print("Left rotate by", k, ":", nums_copy2)
