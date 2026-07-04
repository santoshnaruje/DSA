# Check if array is sorted (ascending or descending)
# Created by santosh

def check_array_is_sorted(nums: list[int]) -> bool:
    ascending = True
    descending = True
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            ascending = False
        if nums[i] < nums[i + 1]:
            descending = False
    return ascending or descending


if __name__ == "__main__":
    nums = [5, 4, 6, 7, 8]
    ans = check_array_is_sorted(nums)
    print(ans)
