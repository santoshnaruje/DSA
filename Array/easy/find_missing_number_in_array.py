# Find missing number in an array of range [0, n]
# Uses XOR trick: XOR of all indices and all values cancels duplicates

def find_missing_number(nums: list[int]) -> int:
    n = len(nums)
    xor_all = 0
    xor_nums = 0
    for i in range(n + 1):
        xor_all ^= i
    for num in nums:
        xor_nums ^= num
    return xor_all ^ xor_nums


if __name__ == "__main__":
    nums = [0, 1, 3, 4, 5]  # missing 2
    print("Missing number:", find_missing_number(nums))
