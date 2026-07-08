# Find the largest element in an array
# Created by santosh

def largest_element(nums: list[int]) -> int:
    largest = float('-inf')
    for num in nums:
        if num > largest:
            largest = num
    return largest


if __name__ == "__main__":
    nums = [6, 3, 8, 10, 16, 7, 5, 2, 9, 14]
    print("Largest element:", largest_element(nums))
