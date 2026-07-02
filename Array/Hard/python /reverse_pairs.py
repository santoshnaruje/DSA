from typing import List


class Solution:

    def countReversepairs(self, nums, low, mid, high):

        count = 0

        right = mid + 1
        for left in range(low, mid + 1):
            while right <= high and nums[left] > 2 * nums[right] :
                right += 1
            count += right - (mid + 1)
        return count

    def merge(self, nums, low, mid, high):

        left = low
        right = mid + 1
        temp = []

        while left <= mid and right <= high:
            if nums[left] < nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1

        while left <= mid:
            temp.append(nums[left])
            left += 1

        while right <= high:
            temp.append(nums[right])
            right += 1

        for i in range(low, high + 1):
            nums[i] = temp[i - low]

    def mergeSort(self, nums, low, high):

        if low >= high:
            return 0

        count = 0
        mid = (low + high) // 2
        count +=self.mergeSort(nums, low, mid)
        count +=self.mergeSort(nums, mid + 1, high)
        count +=self.countReversepairs(nums, low, mid, high)
        self.merge(nums, low, mid, high)
        return count

    def reversePairs(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        return self.mergeSort(nums, low, high)


if __name__ == "__main__":
    nums = [1, 3, 2, 3, 1]
    s = Solution()
    result = s.reversePairs(nums)
    # print(nums)
    print(result)
