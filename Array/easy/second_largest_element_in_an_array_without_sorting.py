# Second largest and second smallest element without sorting
# Created by santosh

def second_largest_element(nums: list[int]) -> dict:
    smallest = float('inf')
    second_smallest = float('inf')
    largest = float('-inf')
    second_largest = float('-inf')

    for num in nums:
        # Largest and second largest
        if num > largest:
            second_largest = largest
            largest = num
        elif num < largest and num > second_largest:
            second_largest = num

        # Smallest and second smallest
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num > smallest and num < second_smallest:
            second_smallest = num

    return {
        "largest": largest,
        "second_largest": second_largest,
        "smallest": smallest,
        "second_smallest": second_smallest,
    }


if __name__ == "__main__":
    nums = [3, 4, 7, 7, 5, 3, 0, 2]
    result = second_largest_element(nums)
    print("Second largest:", result["second_largest"])
    print("Second smallest:", result["second_smallest"])
